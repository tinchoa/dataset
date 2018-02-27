from subprocess import Popen, PIPE
import os, shutil

file=open('new','r')                           # abre-se o arquivo "new2" para leitura: o arquivo
                                                # com os nomes de cada pcap a ser analisado
newFile=open('date-folders.txt','w')

date=[]
a=file.readlines()                              # "a" recebe todas as linhas do arquivo
for i in range(len(a)):                         # para cada linha do arquivo, do
        print 'analizing ' +str(a[i])           # analisando cada pacote
        a[i]=a[i].replace('\n','')              # caracteres de fim de linha sao removidos
        (stdout, stderr) = Popen(["head",a[i]+'/eve.json'], stdout=PIPE).communicate()   # o comando head e enviado ao terminal bash, que retorna as 10 primeiras
                                                                                         # linhas do arquivo .json em questao na variavel stdout.
                                                
        # nestas 4 linhas, a variavel stdout e cortada em pedacos
        # e mantida em listas de acordo com cada palavra de separacao,
        # eventualmente deixando apenas a data do evento.

        b=stdout.split('flow_id')
        aux=b[0].split('timestamp')
        z=aux[1].split('T')
        z=z[0].split(':')[1].split('"')[1]
        if not os.path.exists(z):               # se nao existe um diretorio com tal data:
                os.makedirs(z)                      # cria-se um
                date.append(z)                      # a data de criacao e mudada para a data acima
                newFile.write(z+"/\n")
        shutil.move(a[i],z)                     # e move-se o arquivo para a pasta da data, sendo ela criada agora ou nao.
        os.system("echo "+a[i]+" >> "+z+"/dump-folders.txt")     # aqui, insere-se o nome do pcap analisado num .txt dentro da pasta de data repsectiva
file.close()
newFile.close()
