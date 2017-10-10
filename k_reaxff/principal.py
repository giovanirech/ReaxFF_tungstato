from ase.io import read
from random import getrandbits
import numpy as np
import os
from _differentialevolution import differential_evolution 
from joblib import Parallel, delayed, cpu_count
import time
from filelock import FileLock

imagens = read('imagens_teste.traj', index=':')


caminho_gulp = '/opt/gulp-4.4/Src/gulp'
penalidade = 50000000

arquivo_resultados = 'resultados.txt'
arquivo_modelo_potencial  = 'modelo_potencial_reaxFF.txt'
arquivo_index_bounds = 'index_params_bounds.txt'

def gera_entrada_gulp(P, imagem, nome_arquivo):
    f = open(nome_arquivo + '.gin', 'w')
    f.write('conv prop\n')
    f.write('cell\n')
    f.write('%s %s %s %s %s %s\n'%tuple(imagem.get_cell_lengths_and_angles()))
    f.write('cartesian\n')
    for atom in imagem:
        x, y, z = atom.position
        simbolo = atom.symbol
        f.write( '%s core %s %s %s\n'%(simbolo, x, y, z))
    linhas_potencial_alterado = altera_arquivo_potencial(arquivo_modelo_potencial, P)
    
    for l in linhas_potencial_alterado:
        f.write(l)
        
    f.close()


def altera_arquivo_potencial(arquivo_modelo_potencial, P):
    dic_potenciais = cria_dicionario_potenciais(P)
    with open('../../'+arquivo_modelo_potencial,'r') as f_potencial:
        linhas_modelo_potencial = f_potencial.readlines()        
    linhas_modelo_potencial_alterado = list(linhas_modelo_potencial)        
    chaves = dic_potenciais.keys()

    for c in chaves:
        i = 0
        for l in linhas_modelo_potencial_alterado:
            if c in l:
                linhas_modelo_potencial_alterado[i] = l.replace(c,'%.4f'%(dic_potenciais[c]))
            i = i + 1

    return linhas_modelo_potencial_alterado
    
    
 
def cria_dicionario_potenciais(P):

    i = 0
    dic_potenciais = {}
    for p in P:
        chave = '$' + str(i)
        dic_potenciais[chave] = P[i]
        i = i + 1
    return dic_potenciais

#--------------------------------------------------------

   
def executa_gulp(nome_arquivo):
    os.system('%s < %s.gin > %s.gout'%(caminho_gulp, nome_arquivo, nome_arquivo))
    
def calcula_custo(nome_arquivo, imagem, shift):
    if verifica_final_execucao(nome_arquivo):
        energia_gulp = encontra_energia_gulp(nome_arquivo)
        energia_imagem = imagem.get_potential_energy()
        custo = abs(energia_gulp + shift - energia_imagem)
    else:
        custo = penalidade
    
    return custo

def verifica_final_execucao(nome_arquivo):
    
    f = open(nome_arquivo+'.gout',"r")
    linhas = f.readlines()
    f.close()

    for num,l in enumerate(linhas,0):

        if "error opening file " in l:
            return False

        if l.find("ERROR") != -1:
            return False

        if l.find("Conditions for a minimum have not been satisfied") != -1:
            return False
        
        if l.find("**** Too many reciprocal lattice vectors needed ****") != -1:
            return False

        if l.find("ERROR : Largest core-shell distance exceeds cutoff of cuts") != -1:
            return False
        
        if l.find("ERROR : Cell parameter has fallen below allowed limit") != -1:
            return False

        if l.find("Maximum number of function calls has been reached") != -1:
            return False

        if l.find("**** CPU limit has been exceeded - restart optimisation ****") != -1:
            return False

    return True

def coleta_bounds_do_arquivo(arquivo_index_bounds):
    with open(arquivo_index_bounds, 'r') as f:
        linhas = f.readlines()
    bounds = []
    string_header = ''
    for l in linhas:
        if '$' in l:
            flag, especie, opcao, parametro, minimo, maximo = l.split('\t')
            bounds.append((float(minimo), float(maximo.strip('\n'))))
            string_header = string_header + '\t' + opcao + '_' + parametro + especie
    bounds.append((-30000,30000))#Shift de energia
    string_header = string_header + 'shift_energia\n'
    return bounds, string_header
            

def encontra_energia_gulp(nome_arquivo):
    f = open(nome_arquivo+'.gout',"r")
    linhas = f.readlines()
    f.close()
    
    global penalidade
    
    for l in linhas:
        if 'Total lattice energy' in l:
            return float(l.split()[4])
    return penalidade

def escreve_arquivo_saida(arquivo_resultados,ID,custo,P):
    if os.path.exists(arquivo_resultados):
        append_write = 'a' 
    else:
        append_write = 'w' 
    string_entrada =   str(ID)+'\t'+str(custo)+'\t'
    for p in P:
        string_entrada = string_entrada + str(p) + '\t'
    string_entrada = string_entrada + '\n'
    with open(arquivo_resultados, append_write) as f:
        f.write(string_entrada)  

def acessa_arquivo_lock(arquivo_resultados,ID,custo,P):
    with FileLock('lock'):
        escreve_arquivo_saida(arquivo_resultados,ID,custo,P)
        
def funcao_principal(P):
    #print os.getcwd()
    global imagens, i
    i = getrandbits(64)
    
    
    os.chdir('tmp')
    os.mkdir(str(i))
    os.chdir(str(i))
    
    custos = []
    
    for im in range(np.size(imagens, axis=0)):
        nome_arquivo = 'tungstato_ase_Im' + str(im) + '_Pot' + str(i)
        gera_entrada_gulp(P, imagens[im], nome_arquivo)
        executa_gulp(nome_arquivo)
        custo = calcula_custo(nome_arquivo, imagens[im], P[-1])
        custos.append(custo)
        os.remove(nome_arquivo+'.gin')
        os.remove(nome_arquivo+'.gout')
    custo = np.sum(custos)
    os.chdir('..')
    os.rmdir(str(i))
    os.chdir('..')

    print ' Potencial:%s     Custo: %s \n %s \n###########################################################' %(i, custo, time.ctime())
    #print os.getcwd()
    
    
    #write to file
    acessa_arquivo_lock(arquivo_resultados,i,custo,P)
    
  

    #os.system('rm -r -f tmp/%s'%str(i))
    return custo

#======================================================================================

def pareval(listcoords):
    listresults = Parallel(n_jobs=cpu_count())(delayed(funcao_principal)(i) for i in listcoords) 
    print listresults    
    return listresults

def parallel_run():
    result = differential_evolution(pareval, bounds, parallel=True, polish=False, popsize=5)
    return result

#======================================================================================
if __name__=='__main__':
    bounds, string_header = coleta_bounds_do_arquivo(arquivo_index_bounds)
    start_time = time.time()
    
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    
    
    with open(arquivo_resultados, 'w') as f:
        f.write(string_header)
        
    solution = parallel_run()
    
    print 'parametros:'
    print solution.x
    print 'custo:'
    print solution.fun
    print "Parallel run took %s seconds using %s cores" % ((time.time() - start_time), cpu_count())

