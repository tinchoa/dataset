#!/usr/bin/python

#ataques.py roda em conjunto com varname.py e junta os alertas com o flowtbag

import varname as var
import os, json, traceback, sys

dates = open("date-folders.txt", "r")
a = dates.readlines()
for i in range(len(a)):
    a[i]=a[i].replace('\n','')

    file = open(a[i]+"/alertas-all.log", "r") #abre o arquivo alertas-all de cada pasta que aparece no arquivo "date-folders.txt"
    linha = file.readline()

    ataques = {} #ataques recebe um dicionario vazio

    ataques_id = {} #ataques_id recebe um dicionario vazio
    def add2dict (d, k, valor= None):         #
            if valor == None: valor = {}      # Função para organizar os dados num arquivo 
            if k not in d: d[k] = valor       # json
            else: pass                        #

    print "Tratando alertas-all.log"
    while linha != "":
        print linha
        try:
            dados = linha.split(" ") #cria uma lista separada por espaço a determinada linha do arquivo "alertas-all.log"
            protocolo = dados[-4].strip("{}").strip() #retorna qual protocolo é aquele dado (ex: UDP, TCP)
            bytes = dados[-3].strip().split(":")
            srcip = ":".join(bytes[:-1]) #variavel recebe o IP de origem de cada linha do log
            srcport = bytes[-1] #variavel recebe a Porta de origem de cada linha do log
            bytes = dados[-1].strip().split(":")
            dstip = ":".join(bytes[:-1]) #variavel recebe o IP destino de cada linha do log
            dstport = bytes[-1] #variavel recebe a porta de destino de cada linha do log
            priority = dados[-5].strip("]").strip() #variável recebe o valor da prioriadade
            ataque = " ".join(dados[4:-6]) #expecifica o ataque
        except Exception as e: #tratamento de exceção
            traceback.print_exc(file=sys.stdout)
            print "Linha", linha
        add2dict(ataques, srcip)                               #
        add2dict(ataques[srcip], srcport)                      #Comandos para organizar os 
        add2dict(ataques[srcip][srcport], dstip )              #dados para serem salvos num 
        add2dict(ataques[srcip][srcport][dstip], dstport )     # futuro arquivo json
        add2dict(ataques_id, ataque, 1+len(ataques_id.keys())) #


        ataques[srcip][srcport][dstip][dstport] = (priority,ataques_id[ataque])
        linha = file.readline()

    file.close()

    file = open(a[i]+"/ataques.json","w") #cria/abre um arquivo json
    file.write(json.dumps(ataques)) #escreve no arquivo os ataques (dicionario)
    file.close()

    file = open(a[i]+"/ataques_id.json","w") #cria/abre um arquivo json
    file.write(json.dumps(ataques_id)) #escreve no arquivo os ataques_id (outro dicionario)
    file.close()


    if os.stat(a[i]+"/featuresNew.out").st_size: #verifica se o arquivo "featuresNew.out" está vazio
        print(os.stat(a[i]+"/featuresNew.out").st_size)
        featuresFile = open(a[i]+"/featuresNew.out", "r")
    else: featuresFile = open(a[i]+"/features.out", "r") #abre o arquivo em uma determinada pasta "date" para leitura
    exitFile = open(a[i]+"/classes.out","w") #cria/abre para escrita o arquivo classes.out

    linha = featuresFile.readline()

    print "Tratando Features"
    while linha != "":
        featuresDecoded = linha.strip().split(",") #atribui a variavel uma lista separada por virgulas da linha em analise
        f = featuresDecoded

        try:
            classe = ataques[f[var.srcip]][f[var.srcport]][f[var.dstip]][f[var.dstport]][1] # atribui a variavel o valor numérico da chave do arquivo "ataques_id.json".obs:IP origem -> IP destino
            print "ok"
        except KeyError: #caso não exista esse valor(não é indentificado como ataque), dispara uma exceção
            try:
                classe = ataques[f[var.dstip]][f[var.dstport]][f[var.srcip]][f[var.srcport]][1] # atribui a variavel o valor numérico da chave do arquivo "ataques_id.json". obs: IP destino -> IP origem
                print "ok2"
            except KeyError: #caso não exista esse valor(não é indentificado como ataque), dispara outra exceção
                print "nao eh ataque"
                classe = 0 #significa que não eh ataque, pois não apresenta um valor numérico maior que 0

        f.append(str(classe)) #adicionam mais um campo na lista f
        linha_escreve = ",".join(f) #transforma a lista em uma linha  com formato csv, onde o último campo é o valor numérico da variável classe
        exitFile.write(linha_escreve+"\n")
        linha = featuresFile.readline() #passa para a próxima linha do arquivo "features.out"

    featuresFile.close()
    exitFile.close()

dates.close()
