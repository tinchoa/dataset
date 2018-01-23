
#!/usr/bin/python

from varname import *

hist_ips = {}
hist_ports = {}
hist_par = {}

file = open("features.out")
linha = file.readline().strip().split(",")

while len(linha) > 1 and linha[0] != "":
    if linha[srcip] not in hist_ips:
        hist_ips[linha[srcip]]=1
    else:
        hist_ips[linha[srcip]]+=1
    if int(linha[srcport]) <= 1024:
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