import flowtbag
from flow import features as f
import Queue
from scapy.all import *
import threading
#import MySQLdb
import sys


path =sys.argv[1]
#nomeBase = "dump.pcap"
#nomeBase = "dumpT"
#totalDeArquivos = 27050
janela = 2.
time0 = 0
cdDataset = 1

continuar = True
times = {}
PKTS = []
BUFFER = Queue.Queue()

ENCAPSULAMENTO = PPPoE



def lerDoBuffer():
		oldTimestamp = 0
		print "Comecei a thread de leitura"
		while continuar or not BUFFER.empty():
				pkts = BUFFER.get()
				flows=flowtbag.Flowtbag(pkts)

				for flow in flows.active_flows.values():
						f = str(flow).split(",")
						try:
								timestamp = times[(str(f[0]), int(f[1]),str(f[2]), int(f[3]))]
						except:
								timestamp = oldTimestamp
						oldTimestamp = timestamp

						dado = (timestamp, f)
						dado2 =[timestamp]+f
						for i in dado2:
								arquivo.write(str(i)+',')
						arquivo.write('\n')
						datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dado[0]))
				print "Fim do flowbag"
				print "BUFFER", BUFFER.qsize()
		arquivo.close()
		log.close()

leitura = threading.Thread(target=lerDoBuffer)
leitura.start()


dates = open(path+"date-folders.txt", "r")
a = dates.readlines()
for i in range(len(a)):
	data=a[i].replace('\n','')
	arquivo=open(path+data+'saida-serie.out','w')
	tmp=path+data+'dump-folders.txt'
	read=open(tmp,'r')
	sufixos=read
	#sufixos = [str(i) for i in range (1, 1000)]

	for sufixo in sufixos:
			sufixo=sufixo.replace('\n','')
			print sufixo
			print "\n\n==============================="
			print "Tratando arquivo", sufixo
			print "===============================\n\n"
			
			toRead=path+data+sufixo
			listOfFiles = os.listdir(toRead) 


			packets = rdpcap(toRead+'/'+listOfFiles[2])

			if time0 == 0: time0 = packets[0].time

			for p in packets:
				try:
						if ENCAPSULAMENTO in p: p = p[ENCAPSULAMENTO][1]
						if IP in p and TCP in p[IP]:
							a = (p[IP].src,p[TCP].sport,p[IP].dst,p[TCP].dport)
							if a not in times:
								times[a] = p.time
						elif IP in p and UDP in p[IP]:
							a = (p[IP].src,p[UDP].sport,p[IP].dst,p[UDP].dport)
							if a not in times:
								times[a] = p.time
						else:
								continue
						if p.time - time0 > janela:
							pkts= []
							for pkt in PKTS:
								try:
									pkts.append((len(pkt), str(pkt), pkt.time))
								except RuntimeError:
									pass
							pkts.sort(cmp=lambda x, y: int(1000000000*(x[2] - y[2])))
							BUFFER.put(pkts)
							PKTS = []
							time0 = p.time
						PKTS.append(p)
				except RuntimeError:
						print "RuntimeError"
						print filename
						continue

	continuar = False



