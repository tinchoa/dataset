#!/usr/bin/python

import varname as var
import json, traceback, sys

file = open("fast.log")
linha = file.readline()

ataques = {}

ataques_id = {}
def add2dict (d, k, valor= None):
        if valor == None:
                valor = {}
        if k not in d:
                d[k] = valor
        else:
                pass

print "Tratando Fast.log"
while linha != "":
    print linha
    try:
        dados = linha.split(" ")
        protocolo = dados[-4].strip("{}").strip()
        bytes = dados[-3].strip().split(":")
        srcip = ":".join(bytes[:-1])
        srcport = bytes[-1]
        bytes = dados[-1].strip().split(":")
        dstip = ":".join(bytes[:-1])
        dstport = bytes[-1]
        priority = dados[-5].strip("]").strip()
        ataque = " ".join(dados[4:-6])
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        print "Linha", linha
    add2dict(ataques, srcip)
    add2dict(ataques[srcip], srcport)
    add2dict(ataques[srcip][srcport], dstip )
    add2dict(ataques[srcip][srcport][dstip], dstport )
    add2dict(ataques_id, ataque, 1+len(ataques_id.keys()))


    ataques[srcip][srcport][dstip][dstport] = (priority,ataques_id[ataque])
    linha = file.readline()

file.close()

file = open("ataques.json","w")
file.write(json.dumps(ataques))
file.close()

file = open("ataques_id.json","w")
file.write(json.dumps(ataques_id))
file.close()


featuresFile = open("features-Feb27.out")
exitFile = open("classes.out","w")

linha = featuresFile.readline()

print "Tratando Features"
while linha != "":
    featuresDecoded = linha.strip().split(",")
    f = featuresDecoded

    try:
        classe = ataques[f[var.srcip]][f[var.srcport]][f[var.dstip]][f[var.dstport]][1]
        print "ok"
    except KeyError:
        try:
            classe = ataques[f[var.dstip]][f[var.dstport]][f[var.srcip]][f[var.srcport]][1]
            print "ok2"
        except KeyError:
            print "nao eh ataque"
            classe = 0

    f.append(str(classe))
    linha_escreve = ",".join(f)
    exitFile.write(linha_escreve+"\n")
    linha = featuresFile.readline()

featuresFile.close()
exitFile.close()