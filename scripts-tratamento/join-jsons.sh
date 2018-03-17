#!/bin/bash

#join-jsons.sh junta os alertas format jason de cada pcap e faz um so
#A explicação dos comandos está no arquivo join-alerts.sh, que é praticamente a mesma

path=$1  #passo a rota como argunmento
dates=$path/date-folders.txt

while read -r line1
do
    f="$line1"
    saida=$path/$f/json-all.json
    dumps=$path/$f/dump-folders.txt
    echo 'entering folder '$f
    while read -r line2
    do
	g="$line2"
	echo '----entering folder '$g
	cat $path/$f/$g/eve.json >> $saida #printa o arquivo "eve.json" de cada pcap no final do arquivo "saida"(json-all.json)
    done < "$dumps"
done < "$dates"



