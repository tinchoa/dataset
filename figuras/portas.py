import sys
import json

# calcula o histograma de portas de origem e de destino

count = 0
tcp_src_ports = {}
tcp_dst_ports = {}
udp_src_ports = {}
udp_dst_ports = {}

infile = open('/home/dataset-mobil/nPPoE/2017-11-23/classes.out', 'r')

line = infile.readline()
while line != "":
    count += 1
    features = line.strip().split(',')

    if features[4] == '6': #TCP
    # porta de origem
        if features[1] not in tcp_src_ports:
            tcp_src_ports[features[1]] = [1, 0, 0]  # [total, normais, alertas]
        else:
            tcp_src_ports[features[1]][0] += 1

        if features[-1] == '0':
            tcp_src_ports[features[1]][1] += 1
        else:  # ataques
            tcp_src_ports[features[1]][2] += 1

        # porta de destino
        if features[3] not in tcp_dst_ports:
            tcp_dst_ports[features[3]] = [1, 0, 0]  # [total, normais, alertas]
        else:
            tcp_dst_ports[features[3]][0] += 1

        if features[-1] == '0':
            tcp_dst_ports[features[3]][1] += 1
        else:
            tcp_dst_ports[features[3]][2] += 1

    elif features[4] == '17':  # UDP
        # porta de origem
        if features[1] not in udp_src_ports:
            udp_src_ports[features[1]] = [1, 0, 0]  # [total, normais, alertas]
        else:
            udp_src_ports[features[1]][0] += 1

        if features[-1] == '0':
            udp_src_ports[features[1]][1] += 1
        else:  # ataques
            udp_src_ports[features[1]][2] += 1

        # porta de destino
        if features[3] not in udp_dst_ports:
            udp_dst_ports[features[3]] = [1, 0, 0]  # [total, normais, alertas]
        else:
            udp_dst_ports[features[3]][0] += 1

        if features[-1] == '0':
            udp_dst_ports[features[3]][1] += 1
        else:
            udp_dst_ports[features[3]][2] += 1

    else:
        print "Erro: protocolo diferente de tcp e udp"

    line = infile.readline()

outtcp = open('hist-portas-tcp.csv', 'w')
outudp = open('hist-portas-udp.csv', 'w')
outall = open('hist-portas-all.csv', 'w')


# porta, total_src, normal_src, alerta_src, total_dst, normal_dst, alerta_dst
for i in range(65536):
    key = str(i)
    if key in tcp_src_ports:
        if key in tcp_dst_ports:
            tcpstats = [i, tcp_src_ports[key][0], tcp_src_ports[key][1], tcp_src_ports[key][2], tcp_dst_ports[key][0],tcp_dst_ports[key][1], tcp_dst_ports[key][2]]
        else:
            tcpstats = [i, tcp_src_ports[key][0], tcp_src_ports[key][1], tcp_src_ports[key][2], 0,0,0]
    else:
        if key in tcp_dst_ports:
            tcpstats = [i, 0, 0, 0, tcp_dst_ports[key][0],tcp_dst_ports[key][1], tcp_dst_ports[key][2]]
        else:
            tcpstats = [i, 0, 0, 0, 0, 0, 0]

    if key in udp_src_ports:
        if key in udp_dst_ports:
            udpstats = [i, udp_src_ports[key][0], udp_src_ports[key][1], udp_src_ports[key][2], udp_dst_ports[key][0], udp_dst_ports[key][1], udp_dst_ports[key][2]]
        else:
            udpstats = [i, udp_src_ports[key][0], udp_src_ports[key][1], udp_src_ports[key][2], 0, 0, 0]
    else:
        if key in udp_dst_ports:
            udpstats = [i, 0, 0, 0, udp_dst_ports[key][0], udp_dst_ports[key][1], udp_dst_ports[key][2]]
        else:
            udpstats = [i, 0, 0, 0, 0, 0, 0]

    allstats = [i, tcpstats[1]+udpstats[1],tcpstats[2]+udpstats[2],tcpstats[3]+udpstats[3],tcpstats[4]+udpstats[4],tcpstats[5]+udpstats[5],tcpstats[6]+udpstats[6]]

    outtcp.write(','.join(map(str,tcpstats)) + '\n')
    outudp.write(','.join(map(str, udpstats)) + '\n')
    outall.write(','.join(map(str, allstats)) + '\n')

infile.close()
outtcp.close()
outudp.close()
outall.close()



