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

def gera_entrada_gulp(P, imagem, nome_arquivo):
    f = open(nome_arquivo + '.gin', 'w')
    f.write('conp prop\n')
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
    with open(arquivo_modelo_potencial,'r') as f_potencial:
        linhas_modelo_potencial = f_potencial.readlines()        
    linhas_modelo_potencial_alterado = list(linhas_modelo_potencial)        
    chaves = dic_potenciais.keys()

    for c in chaves:
        i = 0
        for l in linhas_modelo_potencial_alterado:
            if l.find(c) != -1 :
                linhas_modelo_potencial_alterado[i] = l.replace(c,str(dic_potenciais[c]))
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
        custo = abs(energia_gulp+shift-energia_imagem)
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

def encontra_energia_gulp(nome_arquivo):
    f = open(nome_arquivo+'.gout',"r")
    linhas = f.readlines()
    f.close()
    
    global penalidade
    
    for l in linhas:
        if 'Total lattice energy' in l:
            return float(l.split()[4])
    return penalidade

def escreve_arquivo_saida(arquivo_resultados,custo,P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14):
    if os.path.exists(arquivo_resultados):
        append_write = 'a' 
    else:
        append_write = 'w' 
        
    with open(arquivo_resultados, append_write) as f:
        f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(custo,P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14))  

def acessa_arquivo_lock(arquivo_resultados,custo,P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14):
    
    with FileLock('lock'):
        escreve_arquivo_saida(arquivo_resultados,custo,P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14)
        
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
        custo= calcula_custo(nome_arquivo, imagens[im], P[14])
        custos.append(custo)
        os.remove(nome_arquivo+'.gin')
        os.remove(nome_arquivo+'.gout')
    custo = np.sum(custos)
    os.chdir('..')
    os.rmdir(str(i))
    os.chdir('..')

    print (' Potencial:%s '%(i)).center(70, '#')
    print 'Custo: %s'%custo
    print '   Charge core O:%s'%(P[0])
    print '   buck Zr-O: A=%s, rho=%s'%(P[1], P[2])
    print '   buck W-O:  A=%s, rho=%s'%(P[3], P[4])
    print '   buck O-O:  A=%s, rho=%s, C=%s'%(P[5], P[6], P[7])
    print '   spring O:  K= %s'%P[8]
    print '   three O-W-O: k = %s'%(P[9])
    print '   three O-Zr-O: k = %s'%(P[10])
    print '   covexp W-O: D= %s, a= %s, r0= %s'%(P[11], P[12], P[13])
    print '   shift: %s'%P[14]
    print '###########################################################'
    #print os.getcwd()
    
    
    #write to file
    acessa_arquivo_lock(arquivo_resultados,custo,P[0],P[1],P[2],P[3],P[4],P[5],P[6],P[7],P[8],P[9],P[10],P[11],P[12],P[13],P[14])
    
  

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
    bounds=[(0,1), #charge O_core
            (10, 10000),(0.1, 0.5), #buck Zr-O: A, rho
            (10, 10000), (0.1, 0.5), #buck W-O: A, rho
            (10, 30000), (0.1,0.9), (1,100), #buck O-O: A, rho, C
            (5, 90), #spring O
            (0,5.0), #3-body O-Zr-O
            (0,5.0), #3-body O-W-O
            (1, 10), (10,50), (0.1, 3), #covexp W-O: D, a, r0
            (-70000, 0)#shift energia
           ]
    start_time = time.time()
    
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
        
    with open(arquivo_resultados, 'w') as f:
        f.write('#Custo\tchargeO\tbuckZrA\tbuckZrRho\tbuckWA\tbuckWRho\tbuckOA\tbuckORho\tbuckOC\tspringO\t3bOZrO\t3bOWO\tcovexpWD\tcovexpWa\tcovexpWr0\tshiftE\n')
        
    solution = parallel_run()
    
    print 'parametros:'
    print solution.x
    print 'custo:'
    print solution.fun
    print "Parallel run took %s seconds using %s cores" % ((time.time() - start_time), cpu_count())

