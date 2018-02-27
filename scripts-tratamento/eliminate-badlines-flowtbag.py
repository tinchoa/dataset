# checks if features.out has any non-ASCII characters, and removes them if there are.

dates=open('date-folders.txt','r')
a=dates.readlines()
for index in range(len(a)):
    a[index]=a[index].replace('\n','') #retira o "\n" de cada linha no "date-folders.txt"
    fileOld=open(a[index]+'/features.out','r') #abre o arquivo csv para leitura de cada data
    lines=fileOld.readlines()
    fileNew=open(a[index]+'/featuresNew.out','w')#cria o arquivo para escrever o novo csv sem os caractéres non-ASCII

    for i in range(len(lines)):
        e=lines[i].split(',') #separa a linha em uma lista separada por virgulas
        if len(e) == 46:
            k=0
            for j in e:
                if len(j) == 0: k=1
                if k==0: fileNew.write(lines[i])
    fileOld.close()
    fileNew.close()
dates.close()
