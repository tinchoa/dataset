#!/bin/bash

#join-jsons.sh junta os alertas format jason de cada pcap e faz um so
#A explicação dos comandos está no arquivo join-alerts.sh, que é praticamente a mesma

dates=date-folders.txt

while read -r line1
do
    f="$line1"
    saida=$f/json-all.json
    dumps=$f/dump-folders.txt
    echo 'entering folder '$f
    while read -r line2
    do
	g="$line2"
	echo '----entering folder '$g
	cat $f/$g/eve.json >> $saida #printa o arquivo "eve.json" de cada pcap no final do arquivo "saida"(json-all.json)
    done < "$dumps"
done < "$dates"



