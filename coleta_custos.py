from glob import glob
arquivos = glob('./tmp/*/*.custo')

f = open('custos.txt', 'w')

for arquivo in arquivos:
    ID = arquivo.split('/')[2]
    g = open(arquivo,'r')
    custo = float(g.read())
    g.close()
    print '%s\t%s'%(ID,custo)
    f.write('%s\t%s\n'%(ID,custo))
f.close()