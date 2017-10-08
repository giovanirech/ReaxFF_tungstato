#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from random import getrandbits
import os
from matplotlib import use
use('Agg')


caminho_gulp = '/opt/gulp-4.4/Src/'

def cria_arquivo_entrada(id_arquivo, chargeO, buckZrA, buckZrRho, buckWA, buckWRho, buckOA, buckORho, buckOC, springO, threebOZrO, threebOWO, covexpWD, covexpWa, covexpWr0):
    linhas = ['opti prop conp comp free zsisa\n',
              'name alfa-ZrW2O8_2K\n',
              'cell\n',
              '9.18 9.18 9.18 90.000000 90.000000 90.000000\n',
              'fractional\n',
              'Zr core 0.0013 0.0013 0.0013\n',
              'W1 core 0.3405 0.3405 0.3405\n',
              'W2 core 0.59982 0.59982 0.59982\n',
              'O1 core 0.20631 0.4392 0.44700\n',
              'O2 core 0.78662 0.5676 0.55598\n',
              'O3 core 0.49177 0.49177 0.49177\n',
              'O4 core 0.23318 0.23318 0.23318\n',
              'O1 shel 0.20631 0.4392 0.44700\n',
              'O2 shel 0.78662 0.5676 0.55598\n',
              'O3 shel 0.49177 0.49177 0.49177\n',
              'O4 shel 0.23318 0.23318 0.23318\n',
              'space\n',
              '198\n',
              'temperature 2.0\n',
              '\n',
              '###########################################################################\n',
              'name alfa-ZrW2O8_50K\n',
              'cell\n',
              '9.15993 9.15993 9.15993 90.000000 90.000000 90.000000\n',
              'fractional\n',
              'Zr core 0.0003 0.0003 0.0003\n',
              'W1 core 0.3412 0.3412 0.3412\n',
              'W2 core 0.6008 0.6008 0.6008\n',
              'O1 core 0.2071 0.4378 0.4470\n',
              'O2 core 0.7876 0.5694 0.5565\n',
              'O3 core 0.4916 0.4916 0.4916\n',
              'O4 core 0.2336 0.2336 0.2336\n',
              'O1 shel 0.2071 0.4378 0.4470\n',
              'O2 shel 0.7876 0.5694 0.5565\n',
              'O3 shel 0.4916 0.4916 0.4916\n',
              'O4 shel 0.2336 0.2336 0.2336\n',
              'space\n',
              '198\n',
              'temperature 50.0\n',
              '\n',
              '################################################\n',
              '\n',
              '###########################################################################\n',
              'name alfa-ZrW2O8_100K\n',
              'cell\n',
              '9.15993 9.15993 9.15993 90.000000 90.000000 90.000000\n',
              'fractional\n',
              'Zr core 0.0003 0.0003 0.0003\n',
              'W1 core 0.3412 0.3412 0.3412\n',
              'W2 core 0.6008 0.6008 0.6008\n',
              'O1 core 0.2071 0.4378 0.4470\n',
              'O2 core 0.7876 0.5694 0.5565\n',
              'O3 core 0.4916 0.4916 0.4916\n',
              'O4 core 0.2336 0.2336 0.2336\n',
              'O1 shel 0.2071 0.4378 0.4470\n',
              'O2 shel 0.7876 0.5694 0.5565\n',
              'O3 shel 0.4916 0.4916 0.4916\n',
              'O4 shel 0.2336 0.2336 0.2336\n',
              'space\n',
              '198\n',
              'temperature 100.0\n',
              '\n',
              '################################################\n',
              '\n',
              '###########################################################################\n',
              'name alfa-ZrW2O8_150K\n',
              'cell\n',
              '9.15993 9.15993 9.15993 90.000000 90.000000 90.000000\n',
              'fractional\n',
              'Zr core 0.0003 0.0003 0.0003\n',
              'W1 core 0.3412 0.3412 0.3412\n',
              'W2 core 0.6008 0.6008 0.6008\n',
              'O1 core 0.2071 0.4378 0.4470\n',
              'O2 core 0.7876 0.5694 0.5565\n',
              'O3 core 0.4916 0.4916 0.4916\n',
              'O4 core 0.2336 0.2336 0.2336\n',
              'O1 shel 0.2071 0.4378 0.4470\n',
              'O2 shel 0.7876 0.5694 0.5565\n',
              'O3 shel 0.4916 0.4916 0.4916\n',
              'O4 shel 0.2336 0.2336 0.2336\n',
              'space\n',
              '198\n',
              'temperature 150.0\n',
              '\n',
              '################################################\n',
              '\n',
              '###########################################################################\n',
              'name alfa-ZrW2O8_200 K\n',
              'cell\n',
              '9.15993 9.15993 9.15993 90.000000 90.000000 90.000000\n',
              'fractional\n',
              'Zr core 0.0003 0.0003 0.0003\n',
              'W1 core 0.3412 0.3412 0.3412\n',
              'W2 core 0.6008 0.6008 0.6008\n',
              'O1 core 0.2071 0.4378 0.4470\n',
              'O2 core 0.7876 0.5694 0.5565\n',
              'O3 core 0.4916 0.4916 0.4916\n',
              'O4 core 0.2336 0.2336 0.2336\n',
              'O1 shel 0.2071 0.4378 0.4470\n',
              'O2 shel 0.7876 0.5694 0.5565\n',
              'O3 shel 0.4916 0.4916 0.4916\n',
              'O4 shel 0.2336 0.2336 0.2336\n',
              'space\n',
              '198\n',
              'temperature 200.0\n',
              '\n',
              '################################################\n',
              '\n',
              '###########################################################################\n',
              'name alfa-ZrW2O8_250K\n',
              'cell\n',
              '9.15993 9.15993 9.15993 90.000000 90.000000 90.000000\n',
              'fractional\n',
              'Zr core 0.0003 0.0003 0.0003\n',
              'W1 core 0.3412 0.3412 0.3412\n',
              'W2 core 0.6008 0.6008 0.6008\n',
              'O1 core 0.2071 0.4378 0.4470\n',
              'O2 core 0.7876 0.5694 0.5565\n',
              'O3 core 0.4916 0.4916 0.4916\n',
              'O4 core 0.2336 0.2336 0.2336\n',
              'O1 shel 0.2071 0.4378 0.4470\n',
              'O2 shel 0.7876 0.5694 0.5565\n',
              'O3 shel 0.4916 0.4916 0.4916\n',
              'O4 shel 0.2336 0.2336 0.2336\n',
              'space\n',
              '198\n',
              'temperature 250.0\n',
              '\n',
              '################################################\n',
              '\n',
              '###########################################################################\n',
              'name alfa-ZrW2O8_293K\n',
              'cell\n',
              '9.15993 9.15993 9.15993 90.000000 90.000000 90.000000\n',
              'fractional\n',
              'Zr core 0.0003 0.0003 0.0003\n',
              'W1 core 0.3412 0.3412 0.3412\n',
              'W2 core 0.6008 0.6008 0.6008\n',
              'O1 core 0.2071 0.4378 0.4470\n',
              'O2 core 0.7876 0.5694 0.5565\n',
              'O3 core 0.4916 0.4916 0.4916\n',
              'O4 core 0.2336 0.2336 0.2336\n',
              'O1 shel 0.2071 0.4378 0.4470\n',
              'O2 shel 0.7876 0.5694 0.5565\n',
              'O3 shel 0.4916 0.4916 0.4916\n',
              'O4 shel 0.2336 0.2336 0.2336\n',
              'space\n',
              '198\n',
              'temperature 293.0\n',
              '\n',
              '################################################\n',
              'species 4\n',
              'Zr core 4.000000\n',
              'W core 6.000000\n',
              'O core %s\n'%chargeO,
              'O shel %s\n'%(-2-float(chargeO)),
              'buck\n',
              'Zr core O shel %s %s 0.00 0.00 12.00 0 0 0\n'%(buckZrA, buckZrRho),
              'buck\n',
              'W core O shel %s %s 0.00 0.00 12.00 0 0 0\n'%(buckWA,buckWRho),
              'buck\n',
              'O shel O shel %s %s %s 0.00 12.00 0 0 0\n'%(buckOA, buckORho, buckOC),
              'spring\n',
              'O %s 0\n'%(springO),
              '####tres corpos\n',
              'three\n',
              'W core O shel O shel %s 109.47 1.9 1.9 3.0\n'%(threebOWO),
              'Zr core O shel O shel %s 90.0 2.3 2.3 3.0\n'%(threebOZrO),
              '####covexp\n',
              'covexp\n',
              'W core O shel %s %s %s 0.0 2.0 0 0 0\n'%(covexpWD, covexpWa, covexpWr0),
              '#################################################\n',
              'time 4 hours\n',
              '#################################################\n',
              'maxcyc opt 10000\n',
              'dump dump_%s.txt\n'%(id_arquivo)]
    
    with open('%s.gin'%id_arquivo, 'w') as f:
        for l in linhas:
            f.write(l)

            
def verifica_final_execucao(id_arquivo):
    with open('%s.gout'%id_arquivo,'r') as f:
        linhas_arquivo_saida_gulp = f.readlines()

    for num,l in enumerate(linhas_arquivo_saida_gulp,0):

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
        
        if 'Elastic Constant Matrix' in l:
            if '*' in linhas_arquivo_saida_gulp[num+5]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+6]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+7]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+8]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+9]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+10]:
                return False

    return True


#--------------------------------------------------------
def busca_parametros_de_rede(id_arquivo):
    with open('%s.gout'%id_arquivo,'r') as f:
        linhas_arquivo_saida_gulp = f.readlines()
    parametro_rede_a = 0
    fim_config_7 = len(linhas_arquivo_saida_gulp)-1
    for num, linha in enumerate(linhas_arquivo_saida_gulp, 0):
        if 'Output for configuration   1' in linha:
            inicio_config_1 = num
        if 'Output for configuration   2' in linha:
            inicio_config_2 = num
            fim_config_1 = num-1
        if 'Output for configuration   3' in linha:
            inicio_config_3 = num
            fim_config_2 = num-1
        if 'Output for configuration   4' in linha:
            inicio_config_4 = num
            fim_config_3 = num-1
        if 'Output for configuration   5' in linha:
            inicio_config_5 = num
            fim_config_4 = num-1
        if 'Output for configuration   6' in linha:
            inicio_config_6 = num
            fim_config_5 = num-1
        if 'Output for configuration   7' in linha:
            inicio_config_7 = num
            fim_config_6 = num-1
            
    #### parametro a 2K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_1:fim_config_1]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_2K = float(l.split()[1])
            
    #### parametro a 50K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_2:fim_config_2]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_50K = float(l.split()[1])
            
    #### parametro a 100K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_3:fim_config_3]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_100K = float(l.split()[1])
            
    #### parametro a 150K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_4:fim_config_4]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_150K = float(l.split()[1])
            
    #### parametro a 200K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_5:fim_config_5]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_200K = float(l.split()[1])
            
    #### parametro a 250K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_6:fim_config_6]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_250K = float(l.split()[1])

    #### parametro a 293K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_7:fim_config_7]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_293K = float(l.split()[1])
            
    return parametro_rede_a_2K, parametro_rede_a_50K, parametro_rede_a_100K, parametro_rede_a_150K, parametro_rede_a_200K, parametro_rede_a_250K, parametro_rede_a_293K

#--------------------------------------------------------
def busca_constantes_elasticas (id_arquivo):
    with open('%s.gout'%id_arquivo,'r') as f:
        linhas_arquivo_saida_gulp = f.readlines()
        
    fim_config_7 = len(linhas_arquivo_saida_gulp)-1
    for num, linha in enumerate(linhas_arquivo_saida_gulp, 0):
        if 'Output for configuration   1' in linha:
            inicio_config_1 = num
        if 'Output for configuration   2' in linha:
            inicio_config_2 = num
            fim_config_1 = num-1
        if 'Output for configuration   3' in linha:
            inicio_config_3 = num
            fim_config_2 = num-1
        if 'Output for configuration   4' in linha:
            inicio_config_4 = num
            fim_config_3 = num-1
        if 'Output for configuration   5' in linha:
            inicio_config_5 = num
            fim_config_4 = num-1
        if 'Output for configuration   6' in linha:
            inicio_config_6 = num
            fim_config_5 = num-1
        if 'Output for configuration   7' in linha:
            inicio_config_7 = num
            fim_config_6 = num-1
            
   
    ###### constantes a 2K ########        
    c11_2k = 0
    c12_2k = 0
    c44_2k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_1:fim_config_1], inicio_config_1):
        if 'Elastic Constant Matrix' in linha:
            c11_2K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_2K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_2K = float(linhas_arquivo_saida_gulp[num+8][40:50])
            
    ###### constantes a 50K ########        
    c11_50k = 0
    c12_50k = 0
    c44_50k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_2:fim_config_2], inicio_config_2):
        if 'Elastic Constant Matrix' in linha:
            c11_50K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_50K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_50K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 100K ########        
    c11_100k = 0
    c12_100k = 0
    c44_100k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_3:fim_config_3], inicio_config_3):
        if 'Elastic Constant Matrix' in linha:
            c11_100K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_100K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_100K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 150K ########        
    c11_150k = 0
    c12_150k = 0
    c44_150k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_4:fim_config_4], inicio_config_4):
        if 'Elastic Constant Matrix' in linha:
            c11_150K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_150K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_150K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 200K ########        
    c11_200k = 0
    c12_200k = 0
    c44_200k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_5:fim_config_5], inicio_config_5):
        if 'Elastic Constant Matrix' in linha:
            c11_200K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_200K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_200K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 2K ########        
    c11_250k = 0
    c12_250k = 0
    c44_250k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_6:fim_config_6], inicio_config_6):
        if 'Elastic Constant Matrix' in linha:
            c11_250K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_250K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_250K = float(linhas_arquivo_saida_gulp[num+8][40:50])
            
    ###### constantes a 293K ########        
    c11_293k = 0
    c12_293k = 0
    c44_293k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_7:fim_config_7], inicio_config_7):
        if 'Elastic Constant Matrix' in linha:
            c11_293K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_293K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_293K = float(linhas_arquivo_saida_gulp[num+8][40:50])

    return (c11_2K, c12_2K, c44_2K,
            c11_50K, c12_50K, c44_50K,
            c11_100K, c12_100K, c44_100K,
            c11_150K, c12_150K, c44_150K,
            c11_200K, c12_200K, c44_200K,
            c11_250K, c12_250K, c44_250K,
            c11_293K, c12_293K, c44_293K)

#---------------------------------------------------------------
def coleta_potencial_por_indice(indice):
    with open('enum_resultados.txt', 'r') as f:
        linhas = f.readlines()
    print linhas[indice]
    return linhas[indice].split('\t')[1:]

#------------------------------------------------
def testa_potencial_grafico(chargeO, buckZrA, buckZrRho, buckWA, buckWRho, buckOA, buckORho, buckOC, springO, threebOZrO, threebOWO, covexpWD, covexpWa, covexpWr0):
    id_arquivo = getrandbits(64)
    print 'ID de arquivo:%s'%id_arquivo
    os.mkdir(str(id_arquivo))
    os.chdir(str(id_arquivo))
    cria_arquivo_entrada(id_arquivo, chargeO, buckZrA, buckZrRho, buckWA, buckWRho, buckOA, buckORho, buckOC, springO, threebOZrO, threebOWO, covexpWD, covexpWa, covexpWr0)
    print 'Executando GULP... Isto pode demorar vários minutos'
    os.system('timeout 10800 %sgulp < %s.gin > %s.gout'%(caminho_gulp, id_arquivo, id_arquivo))
    finalizou_sem_erros = verifica_final_execucao(id_arquivo)
    if not finalizou_sem_erros:
        print 'Erro na execução do arquivo GULP. Este potencial pode ser inválido. Verifique o arquivo %s.gin para mais detalhes'%(id_arquivo)
    else:
        T_calc = np.asarray([2, 50, 100 ,150, 200, 250, 293])
        par_calc = np.asarray(busca_parametros_de_rede(id_arquivo))
        (c11_2K, c12_2K, c44_2K, c11_50K, c12_50K, c44_50K, c11_100K, c12_100K, c44_100K, c11_150K, c12_150K, c44_150K, c11_200K, c12_200K, c44_200K, c11_250K, c12_250K, c44_250K, c11_293K, c12_293K, c44_293K) = busca_constantes_elasticas(id_arquivo)
        c11_calc = np.asarray([c11_2K, c11_50K, c11_100K, c11_150K, c11_200K, c11_250K, c11_293K])
        c44_calc = np.asarray([c44_2K, c44_50K, c44_100K, c44_150K, c44_200K, c44_250K, c44_293K])
        
        #Grafico
        fig = plt.figure(figsize=(8,15))
        
        #Parametrode rede#
        ax1 = fig.add_subplot(3,1,1)
        plt.plot(T_parametro_exp, parametro_exp, 'o', label='Experimental')
        plt.plot(T_calc, par_calc, label='Potencial %s'%id_arquivo)
        ax1.set_xlim(0,300)
        ax1.set_xlabel('Temperatura (K)')
        ax1.set_ylabel('Parametro de rede (A)')
        ax1.legend()
        
        ###  C11 #####
        ax2 = fig.add_subplot(3, 1, 2)
        plt.plot(T_c11_exp, c11_exp, 'o', label = 'Experimental')
        plt.plot(T_calc, c11_calc, label='Potencial %s'%id_arquivo)
        ax2.set_xlim(0,300)
        ax2.set_xlabel('Temperatura (K)')
        ax2.set_ylabel('C$\mathbf{_{11}}$ (GPa)')
        ax2.legend()
        
        ### C44 ###
        ax3 = fig.add_subplot(3, 1, 3)
        plt.plot(T_c44_exp, c44_exp, 'o', label = 'Experimental')
        plt.plot(T_calc, c44_calc, label='Potencial %s'%id_arquivo)
        ax3.set_xlim(0,300)
        ax3.set_xlabel('Temperatura (K)')
        ax3.set_ylabel('C$\mathbf{_{44}}$ (GPa)')
        ax3.legend()
        
        plt.tight_layout()
        plt.savefig('%s.png'%id_arquivo)
        
    os.chdir('..')


#Dados experimentais
T_parametro_exp = np.asarray([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,204,206,208,210,212,214,216,218,220,222,224,226,228,230,232,234,236,238,240,242,244,246,248,250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324,326,328,330,332,334,336,338,340,342,344,346,348,350,352,354,356,358,360,362,364,366,368,370,372,374,376,378,380,382,384,386,388,390,392,394,396,398,400,402,404,406,408,410,412,414,416,418,420,422,424,426,428,430,432,434,436,438,440,442,444,446,448,450,452,454,456,458,460,462,464,466,468,470,472,474,476,478,480,482,484,486,488,490,492,494,496,498,500,502,504,506,508,510,512,514,516,518,520])
parametro_exp = np.asarray([9.18,9.17999,9.18003,9.18002,9.18002,9.17997,9.17997,9.17987,9.17981,9.17967,9.17962,9.17953,9.1794,9.17929,9.17914,9.17901,9.17891,9.17877,9.17861,9.17849,9.17826,9.17811,9.17798,9.17785,9.17766,9.1775,9.17735,9.17715,9.17698,9.17685,9.17665,9.17644,9.1763,9.17612,9.17596,9.17572,9.17556,9.1754,9.1752,9.175,9.17486,9.17466,9.17445,9.17426,9.17407,9.17391,9.17372,9.1735,9.17331,9.17312,9.17298,9.17281,9.17261,9.17242,9.17223,9.17206,9.17189,9.17166,9.1715,9.1713,9.17113,9.17093,9.17078,9.17049,9.17031,9.1702,9.16996,9.16978,9.16959,9.16941,9.1692,9.16901,9.16882,9.16865,9.16846,9.16822,9.16807,9.16789,9.16769,9.16748,9.16729,9.16708,9.16692,9.16673,9.16654,9.16636,9.16616,9.16606,9.16584,9.16567,9.16545,9.16529,9.16512,9.16496,9.16481,9.16455,9.16441,9.16425,9.16409,9.16393,9.16372,9.16352,9.16336,9.16318,9.163,9.16284,9.16262,9.1625,9.16225,9.16217,9.16194,9.16178,9.16161,9.16144,9.16124,9.16111,9.16092,9.16076,9.1606,9.16042,9.16025,9.16005,9.15991,9.15973,9.15955,9.15935,9.15922,9.15905,9.15888,9.15867,9.15852,9.15835,9.15818,9.15804,9.15784,9.15769,9.15752,9.1573,9.15716,9.15702,9.15682,9.15668,9.15647,9.1563,9.15614,9.15597,9.15579,9.15564,9.15549,9.15531,9.15512,9.15499,9.15481,9.15464,9.15443,9.15434,9.15417,9.15396,9.15375,9.15361,9.15343,9.15327,9.15316,9.15292,9.15277,9.15265,9.15232,9.15219,9.15205,9.15195,9.15171,9.15157,9.15136,9.1513,9.15101,9.15085,9.15065,9.15056,9.15039,9.15014,9.15005,9.14985,9.14967,9.1495,9.14935,9.14919,9.14894,9.14884,9.14863,9.14838,9.1482,9.14796,9.14807,9.14797,9.14778,9.14762,9.14754,9.14735,9.14718,9.14702,9.14677,9.14654,9.14637,9.14617,9.14593,9.14565,9.14539,9.14521,9.14498,9.14468,9.14438,9.14415,9.14388,9.14354,9.14324,9.14296,9.14266,9.14229,9.14189,9.14161,9.14126,9.1408,9.14036,9.13994,9.13944,9.13912,9.13889,9.13871,9.13851,9.13837,9.13822,9.13818,9.138,9.13786,9.13773,9.13767,9.13754,9.13741,9.13734,9.1372,9.13706,9.13698,9.13691,9.13678,9.13664,9.13651,9.13636,9.13635,9.13623,9.1361,9.136,9.13598,9.13587,9.13532,9.13528,9.13521,9.13509,9.13508,9.13496,9.13489])
T_c44_exp = np.asarray([   4.38215,    9.39326,   13.6219 ,   18.5204 ,   23.4174 , 27.7601 ,   32.6579 ,   38.3357 ,   43.3446 ,   48.6893 , 53.6981 ,   58.9295 ,   63.9381 ,   68.6144 ,   74.848  , 79.746  ,   84.9778 ,   89.4319 ,   94.663  ,  100.008  ,104.682  ,  109.691  ,  114.701  ,  119.601  ,  124.72   ,129.618  ,  134.628  ,  139.194  ,  144.09   ,  149.992  ,155.112  ,  158.674  ,  163.796  ,  169.027  ,  173.704  ,180.049  ,  184.948  ,  189.958  ,  194.745  ,  199.976  ,204.876  ,  210.33   ,  215.007  ,  220.242  ,  225.029  ,230.82   ,  235.718  ,  240.729  ,  246.184  ,  251.082  ,256.426  ,  261.211  ,  267.447  ,  272.678  ,  277.353  ,282.139  ,  287.149  ,  292.048  ,  297.166  ])
c44_exp =  np.asarray([29.288956 ,  29.288408 ,  29.223744 ,  29.196344 ,  29.136886 ,29.131132 ,  29.087566 ,  29.05496  ,  29.006188 ,  28.994954 ,28.946182 ,  28.89193  ,  28.837678 ,  28.821238 ,  28.766986 ,28.7289   ,  28.685334 ,  28.67958  ,  28.620122 ,  28.608888 ,28.554636 ,  28.505864 ,  28.483944 ,  28.47271  ,  28.413252 ,28.369686 ,  28.347766 ,  28.342012 ,  28.277074 ,  28.271046 ,28.222274 ,  28.189668 ,  28.178434 ,  28.118976 ,  28.118428 ,28.064176 ,  28.036776 ,  28.00965  ,  27.97677  ,  27.927998 ,27.92745  ,  27.873472 ,  27.867444 ,  27.904434 ,  27.855662 ,27.881966 ,  27.833194 ,  27.837852 ,  27.79456  ,  27.76168  ,27.734554 ,  27.664136 ,  27.647422 ,  27.59865  ,  27.560564 ,27.49042  ,  27.484666 ,  27.467952 ,  27.3548722])
T_c11_exp = np.asarray([   4.73582,    9.97064,   13.8652 ,   18.761  ,   23.8802 , 28.2192 ,   33.0029 ,   38.7878 ,   44.0149 ,   48.9102 , 54.0248 ,   58.9218 ,   64.0361 ,   68.7059 ,   74.9363 , 79.9404 ,   84.9443 ,   89.8384 ,   94.9529 ,  100.07   ,104.963  ,  109.971  ,  114.864  ,  119.977  ,  125.208  ,129.992  ,  134.997  ,  140.002  ,  145.118  ,  150.124  ,155.24   ,  159.022  ,  164.027  ,  169.143  ,  174.149  ,179.934  ,  185.05   ,  190.168  ,  195.173  ,  200.289  ,205.407  ,  210.413  ,  215.084  ,  220.2    ,  225.318  ,231.102  ,  236.106  ,  241.002  ,  246.118  ,  251.123  ,256.129  ,  261.023  ,  266.912  ,  271.924  ,  277.151  ,282.04   ,  287.271  ,  292.944  ,  298.95   ])
c11_exp = np.asarray([ 161.791704,  161.889288,  161.586264,  161.181804,  160.8531  ,160.44864 ,  159.969708,  159.388056,  158.707536,  158.253   ,157.446648,  157.16802 ,  156.337272,  155.605392,  155.025024,154.318824,  153.588228,  153.00786 ,  152.201508,  151.6725  ,150.9663  ,  150.637596,  149.981472,  149.024892,  148.720584,148.215972,  147.609924,  146.97948 ,  146.399112,  145.844424,145.21398 ,  144.735048,  144.104604,  143.498556,  142.943868,142.38918 ,  141.783132,  141.228444,  140.622396,  140.017632,139.537416,  139.0572  ,  138.452436,  137.771916,  137.267304,136.5855  ,  135.90498 ,  135.5262  ,  134.84568 ,  134.239632,133.684944,  133.130256,  131.7705  ,  131.91816 ,  131.213244,130.155228,  129.800844,  129.1704  ,  128.43852 ])

#Le potencial de input
#Custo chargeO buckZrA buckZrRho buckWA buckWRho buckOA buckORho buckOC springO 3bOZrO 3bOWO covexpWD covexpWa covexpWr0 shiftE
if len(sys.argv)<2:
    print u'O número correto (15 ou 1) de argumentos deve ser fornecido. Utilize -h para mais informaçoes'
elif str(sys.argv[1])=='-h':
    print u'Forneça os parametros de potencial na seguinte ordem'
    print 'chargeO buckZrA buckZrRho buckWA buckWRho buckOA buckORho buckOC springO 3bOZrO 3bOWO covexpWD covexpWa covexpWr0 shiftE'
    print 'alternativamente, você pode fornecer o indice do potencial contido no arquivo enum_resultados.txt gerado pelo script enumera_resultados.py'
elif len(sys.argv) == 2:
    indice_potencial = int(sys.argv[1])
    (Custo, chargeO, buckZrA, buckZrRho, buckWA, buckWRho, buckOA, buckORho, buckOC, springO, threebOZrO, threebOWO, covexpWD, covexpWa, covexpWr0, shiftE) = coleta_potencial_por_indice(indice_potencial)
    print '--> Custo: %s'%Custo
    print 'Potencial selecionado:'
    print '   Carga O_core: %s'%chargeO
    print '   Buckingham Zr-O: A= %s,  rho= %s,  C= 0'%(buckZrA, buckZrRho)
    print '   Buckingham W-O: A= %s,  rho= %s,  C= 0'%(buckWA, buckWRho)
    print '   Buckingham O-O: A= %s,  rho= %s,  C= %s'%(buckOA, buckORho, buckOC)
    print '   Spring O_core-O_shell: %s'%springO
    print '   3-Body O-Zr-O: %s'%threebOZrO
    print '   3-Body O-W-O: %s'%threebOWO 
    print '   Covexp W-O: D= %s,  a= %s,  r0=%s'%(covexpWD,covexpWa,covexpWr0) 
    print '   Shift Energia: %s'%shiftE
    testa_potencial_grafico(chargeO, buckZrA, buckZrRho, buckWA, buckWRho, buckOA, buckORho, buckOC, springO, threebOZrO, threebOWO, covexpWD, covexpWa, covexpWr0)
elif len(sys.argv)!=16:
    print u'O número correto (15 ou 1) de argumentos deve ser fornecido. Utilize -h para mais informaçoes'
else:
    chargeO = sys.argv[1]
    buckZrA = sys.argv[2]
    buckZrRho = sys.argv[3]
    buckWA = sys.argv[4]
    buckWRho = sys.argv[5]
    buckOA = sys.argv[6]
    buckORho = sys.argv[7]
    buckOC = sys.argv[8]
    springO = sys.argv[9]
    threebOZrO = sys.argv[10]
    threebOWO = sys.argv[11]
    covexpWD = sys.argv[12]
    covexpWa  = sys.argv[13]
    covexpWr0 = sys.argv[14]
    shiftE = sys.argv[15]
    print 'Potencial selecionado:'
    print '   Carga O_core: %s'%chargeO
    print '   Buckingham Zr-O: A= %s,  rho= %s,  C= 0'%(buckZrA, buckZrRho)
    print '   Buckingham W-O: A= %s,  rho= %s,  C= 0'%(buckWA, buckWRho)
    print '   Buckingham O-O: A= %s,  rho= %s,  C= %s'%(buckOA, buckORho, buckOC)
    print '   Spring O_core-O_shell: %s'%springO
    print '   3-Body O-Zr-O: %s'%threebOZrO
    print '   3-Body O-W-O: %s'%threebOWO 
    print '   Covexp W-O: D= %s,  a= %s,  r0=%s'%(covexpWD,covexpWa,covexpWr0) 
    print '   Shift Energia: %s'%shiftE
    testa_potencial_grafico(chargeO, buckZrA, buckZrRho, buckWA, buckWRho, buckOA, buckORho, buckOC, springO, threebOZrO, threebOWO, covexpWD, covexpWa, covexpWr0)

        
