#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import use
use('Agg')

import matplotlib.pyplot as plt

with open('resultados.txt', 'r') as f:
    linhas = f.readlines()
    
minimo = float(linhas[1].split()[0])
M = []
for n, linha in enumerate(linhas[1:],0):
    custo = float(linha.split()[0])
    minimo = min(custo, minimo)
    M.append([n, minimo])
    
M = np.asarray(M)

fig=plt.figure(figsize=(8,5))
plt.semilogy(M[:,0], M[:,1], lw=2)
plt.xlabel('n')
plt.ylabel(u'Custo mínimo (eV)')
plt.grid()
plt.grid(axis='y', which='minor')
plt.savefig('status.png')
