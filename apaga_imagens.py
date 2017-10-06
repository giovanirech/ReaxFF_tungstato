# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 18:48:48 2017

@author: giovani
"""

import os

lista_pastas = os.listdir('tmp/')
N = len(lista_pastas)
n = 0
for pasta in lista_pastas:
    if os.path.exists('tmp/%s/tungstato_ase_Im0_Pot%s.gin'%(pasta, pasta)):
        os.system('cp tmp/%s/tungstato_ase_Im0_Pot%s.gin tmp/%s/%s.gin'%(pasta, pasta, pasta, pasta))
        os.system('cp tmp/%s/tungstato_ase_Im0_Pot%s.gout tmp/%s/%s.gout'%(pasta, pasta, pasta, pasta))
        os.system('rm tmp/%s/tungstato_ase*'%pasta)
    print '%.2f'%(100*float(n)/float(N))
    n += 1