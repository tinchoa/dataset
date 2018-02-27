from datetime import datetime
fmt="%m/%d/%Y-%H:%M:%S.%f"

dates = open("date-folders.txt", "r")
folder = dates.readlines()
for i in range(len(folder)):
    
    folder[i]=folder[i].replace('\n','')
    file = open(folder[i]+"/alertas-all.log","r")
    linha = file.readline()
    alerts = []
    while linha:
        a = linha.strip("\n").split(" ")
        alerts.append(a)
        linha = file.readline()

    newFile = open(folder[i]+"/dictionaries.txt", "w")

    tipoDeAlerta= {}

    # os tipos de alertas estao, dentro dos arquivos alertas-all.log, presentes entre marcadores
    # do tipo "[**]". Neste loop, esta secao e identificada e pareada, num dicionario,
    # com o IP de origem (src), o de destino (dst) e o timestamp (time)

    for alert in alerts:
        j, k, l = [0] * 3 # indices de marcacao de "[**]"
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

    # verifica os tipos de alertas para cada IP de destino encontrado
    # e pareia esses dados num dicionario

    alertasPorHost = {}
    for k in tipoDeAlerta:
        for i in tipoDeAlerta[k]:
            ipDst = i[-1].split(":")[0]
            if ipDst not in alertasPorHost:
                alertasPorHost[ipDst] = []
            alertasPorHost[ipDst].append(k)

    # calcula quantos alertas distintos existem para cada IP de destino
    # e pareia esses dados num dicionario

    numeroAlertas = {}
    for k in alertasPorHost:
        setAlertas = set(alertasPorHost[k])
        numeroAlertas[k] = len(setAlertas)
    newFile.write(str(numeroAlertas)+"\n")

    # calcula a quantidade de IP's com o mesmo numero de alertas distintos
    # e pareia esses dados num dicionario

    histAlertas = {}
    for i in numeroAlertas.values():
        if i not in histAlertas: histAlertas[i]=0
        histAlertas[i]+=1
    newFile.write(str(histAlertas))
    newFile.close()
dates.close()
