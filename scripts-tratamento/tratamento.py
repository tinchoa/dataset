import json, os
#fmt="%d/%m/%Y-%H:%M:%S.%f"
fmt='%Y-%m-%dT%H:%M:%S.%f-0200'
from dateutil.parser import parse
from datetime import datetime
import csv

#arquivo=open('eve-test.json','r')

# aqui se usa um loop de for para entrar nas pastas de cada dia 
dates = open("date-folders.txt", "r")
a = dates.readlines()
for i in range(len(a)):

    a[i]=a[i].replace('\n','')
    arquivo=open(a[i]+'/json-all.json','r')
    w = csv.writer(open(a[i]+"/output.csv", "w"))
    file2 = open(a[i]+"/times.txt", "w")

    lines=arquivo.readlines()

    flows={} #has flow_id as keys
    stats={} #has stats
    ips={} #has ips as keys
    alerts=[]  #alerst
    timeStamp={} #to analize the moment of the day alert

    p=0
    os.system('clear')  # on linux / os x
    print 'calculating All'
    for i in lines:
            p+=1
            # print p%10
            if p % 100000 == 0:
                    print p

            dumps=json.loads(i)

            if dumps['event_type'] != u'stats':
                    if 'alert' in dumps.values():
                            # if dumps['alert'] not in alerts: #getting alerts
                            #       alerts[dumps['alert']]=[dumps]
                            # else:
                            #       alerts[dumps['alert']].append(dumps)
                            alerts.append(dumps['alert'])
                    else:
                            if dumps['flow_id'] not in flows: #getting the flows
                                    flows[dumps['flow_id']]=[dumps]
                            else:
                                    flows[dumps['flow_id']].append(dumps)

                            if dumps['dest_ip'] not in ips: #getting ips
                                    ips[dumps['dest_ip']]=[dumps]
                            else:
                                    ips[dumps['dest_ip']].append(dumps)
                    if datetime.strptime(dumps['timestamp'],fmt) not in timeStamp: #getting timestamps and converting to dateTime
                                    #timeStamp[datetime.strptime(dumps['timestamp'],fmt)]=[datetime.strptime(dumps['timestamp'],fmt)]
                                    timeStamp[datetime.strptime(dumps['timestamp'],fmt)]=1
                    else:
            #               timeStamp[datetime.strptime(dumps['timestamp'],fmt)].append(datetime.strptime(dumps['timestamp'],fmt))
                            timeStamp[datetime.strptime(dumps['timestamp'],fmt)]+=1
            else:
                    stats['event_type']=dumps



    for key, value in sorted(timeStamp.iteritems(), key=lambda (k,v): (v,k)):#sort the timestamp
                    file2.write(str(key)+', '+str(value)+' \n')


    #dividir alertas pelas horas
    #pensei em agrupar em bloques de 4 em 4 hs ([00 a 4 am][5am 9am][10am 14pm][15pm 19][20pm 24])

    number={}

    for i in ips.keys(): #getting the number of flows for each IP
            for j in ips[i]:
                    number[i]=len(ips[i])

    number_sorted=sorted(number.items(), key=lambda x:x[1], reverse=True)


    ports={} #getting destination ports and timestamp for each
    os.system('clear')  # on linux / os x
    print 'calculating IPS'
    p=0
    for i in ips.keys():
            # p+=1
            # print p%10
            ports[i]=[]
            for j in ips[i]: #get ports for each ip
                    if 'dest_port' in j:
                            if ports[i] == j[u'dest_port'] :
                                    ports[i]=[j[u'dest_port'],(parse(j[u'timestamp']))]
                            else:
                                    ports[i].append([j[u'dest_port'],(parse(j[u'timestamp']))])
                    else:
                            ports[i].append('0') #in some cases in IPV6 there is no port
                    #print str(i)+ ' port ' +str(j[u'dest_port'])

    for i in ports:
            ports[i].sort() #order

    for key, val in ports.items():
            w.writerow([key, val])
    p=0
    os.system('clear')  # on linux / os x
    print 'calculating times'
    devTime={}
    # p+=1
    # print p%10
    for i in ports.keys(): #getting avg time btwn flows
            j=0
            k=1
            devTime[i]=[]
            while j < len(ports[i])-1:
                    while j+k < len(ports[i]) and ports[i][j+k] == '0': k+=1
                    if j+k < len(ports[i]):
                        aux = ports[i][j+k][1] - ports[i][j][1]
                        devTime[i].append(aux.total_seconds())
                    j+=k
                    k=1
dates.close()
