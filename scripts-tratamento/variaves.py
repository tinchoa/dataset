#!/usr/bin/python
from varname import *   # variaveis como srcip e dstip sao importadas
                        # do arquivo varname.py
import os

dates = open("date-folders.txt", "r")
folder = dates.readlines()
for i in range(len(folder)):
    
    folder[i]=folder[i].replace('\n','')
    
    # aqui, conta-se quantas vezes: um mesmo IP de origem aparece,
    # um mesmo par de IP [origem, destino] aparece,
    # e uma mesma porta aparece no arquivo features.out

    hist_ips = {}
    hist_ports = {}
    hist_par = {}

    if os.stat(folder[i]+"/featuresNew.out").st_size:
        print(os.stat(folder[i]+"/featuresNew.out").st_size)
        file = open(folder[i]+"/featuresNew.out")
    else: file = open(folder[i]+"/features.out")

    linha = file.readline().strip().split(",")

    while len(linha) > 1 and linha[0] != "":
        if linha[srcip] not in hist_ips:
            hist_ips[linha[srcip]]=1
        else:
            hist_ips[linha[srcip]]+=1
        if int(linha[srcport]) <= 1024:     # sao contadas apenas as portas menores ou iguais a 1024
                if linha[srcport] not in hist_ports:
                    hist_ports[linha[srcport]]=1
                else:
                    hist_ports[linha[srcport]]+=1
        if int(linha[dstport]) <= 1024:
                if linha[dstport] not in hist_ports:
                    hist_ports[linha[dstport]]=1
                else:
                    hist_ports[linha[dstport]]+=1
        par = [linha[srcip], linha[dstip]]
        par.sort()
        if str(par) not in hist_par:
            hist_par[str(par)]=1
        else:
            hist_par[str(par)]+=1
        try: linha = file.readline().strip("\n").split(",")
        except: linha =""
    newFile = open(folder[i]+"/dictionaries1.txt", "w")
    newFile.write(str(hist_ips)+"\n")
    newFile.write(str(hist_par)+"\n")
    newFile.write(str(hist_ports))
dates.close()
