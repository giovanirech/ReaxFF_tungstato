# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:22:18 2017

@author: giovani
"""
import numpy as np
import os

def procura_parametros(arquivo):
    gin = open(arquivo, 'r')
    linhas = gin.readlines()
    gin.close()
    charge_o = float(linhas[83].strip('\n').split()[-1])
    buck_zr_a, buck_zr_r = linhas[86].split()[4:6]
    buck_w_a, buck_w_r = linhas[88].split()[4:6]
    buck_o_a, buck_o_r, buck_o_c = linhas[90].split()[4:7]
    spring_o = linhas[92].split()[1]
    three_w = linhas[95].split()[6]
    three_zr = linhas[96].split()[6]
    covexp_w_d, covexp_w_a, covexp_w_r0 = linhas[99].split()[4:7]
    return charge_o, buck_zr_a, buck_zr_r, buck_w_a, buck_w_r, buck_o_a, buck_o_r, buck_o_c, spring_o, three_w, three_zr, covexp_w_d, covexp_w_a, covexp_w_r0

lista_pastas = os.listdir('tmp/')
n=0
N=len(lista_pastas)
f = open('resumo.txt', 'w')
f.write('#custo\tid_pot\tcharge_o\tbuck_zr_a\tbuck_zr_r\tbuck_w_a\tbuck_w_r\tbuck_o_a\tbuck_o_r\tbuck_o_c\tspring_o\tthree_w\tthree_zr\tcovexp_w_d\tcovexp_w_a\tcovexp_w_r0\n')

for pasta in lista_pastas:
    print '%.2f%%'%(100*float(n)/float(N))
    n += 1    
    if os.path.exists('tmp/%s/%s.custo'%(pasta, pasta)):
            id_string = pasta
            custo = np.genfromtxt('tmp/%s/%s.custo'%(pasta, pasta))
            charge_o, buck_zr_a, buck_zr_r, buck_w_a, buck_w_r, buck_o_a, buck_o_r, buck_o_c, spring_o, three_w, three_zr, covexp_w_d, covexp_w_a, covexp_w_r0 = procura_parametros('tmp/%s/%s.gin'%(pasta, pasta))
            f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(custo, id_string, charge_o, buck_zr_a, buck_zr_r, buck_w_a, buck_w_r, buck_o_a, buck_o_r, buck_o_c, spring_o, three_w, three_zr, covexp_w_d, covexp_w_a, covexp_w_r0))
    else:
        print 'Path tmp/%s/%s.custo does not exists!'%(pasta, pasta)
f.close()