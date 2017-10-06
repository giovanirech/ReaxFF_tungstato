from glob import glob
import numpy as np
import os
arquivos = glob('tmp/*/*.custo')
custos = []
N = len(arquivos)
custo_maximo = 30000
for n,path in enumerate(arquivos,0):
    pot = path.split('/')[-1].strip('.custo')
    custo = float(np.genfromtxt(path))
    custos.append(custo)
    print '%.2f%% completed'%(100*float(n)/float(N))
    if custo <= custo_maximo:
        os.system('rm -r '+path.rpartition('/')[0])
        print 'Directory removed: %s'%path
