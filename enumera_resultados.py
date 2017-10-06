with open('resultados.txt','r') as f:
    linhas = f.readlines()[1:]
minimo = linhas[0].split('\t')[0]
i_minimo=0
with open('enum_resultados.txt','w') as f:
    for n,l in enumerate(linhas,0):
        f.write('%s\t%s'%(n, l))
        c = float(l.split('\t')[0])
        if c<minimo:
            minimo = c
            i_minimo = n
print 'Menor custo:%s  com indice: %s'%(minimo, i_minimo)