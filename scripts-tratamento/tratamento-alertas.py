from datetime import datetime
fmt="%d/%m/%Y-%H:%M:%S.%f"

file = open("fast.log","r")
linha = file.readline()
alerts = []
while linha:
    a = linha.strip("\n").split(" ")
    alerts.append(a)
    linha = file.readline()

tipoDeAlerta= {}

for alert in alerts:
    j, k, l = [0] * 3
    while j < len(alert):
        if alert[j] == '[**]':
            if k == 0:
                k = j
                l = j
            if l == k: l = j
        j+= 1
    attack = " ".join(alert[k+2:l])
    src = alert[-3]
    dst = alert[-1].strip("\r")
    time = alert[0]
    if attack not in tipoDeAlerta:
        tipoDeAlerta[attack] = []
    tipoDeAlerta[attack].append((datetime.strptime(time,fmt),src,dst))

alertasPorHost = {}
for k in tipoDeAlerta:
    for i in tipoDeAlerta[k]:
        ipDst = i[-1].split(":")[0]
        if ipDst not in alertasPorHost:
            alertasPorHost[ipDst] = []
        alertasPorHost[ipDst].append(k)

numeroAlertas = {}
for k in alertasPorHost:
    setAlertas = set(alertasPorHost[k])
    numeroAlertas[k] = len(setAlertas)

histAlertas = {}
for i in numeroAlertas.values() :
    if i not in histAlertas: histAlertas[i]=0
    histAlertas[i]+=1