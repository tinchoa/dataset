#!/bin/bash

#Join-alerts.sh junta os alertas (fast.log) de cada pcap e faz um so
path=$1

dates=$path/date-folders.txt

while read -r line1 #retorna o valor de cada linha do arquivo "dates" a variável line1 em cada loop 
do
    f="$line1" #atribui a variável f o valor de uma determinada linha do arquivo "date" em questão
    saida=$path/$f/alertas-all.log
    dumps=$path/$f/dump-folders.txt
    echo 'entering folder '$f
    while read -r line2 #retorna o valor de cada linha do arquivo "dumps" a variavel line2 em cada loop
    do
	g="$line2"
	echo '----entering folder '$g
	cat $path/$f/$g/fast.log >> $saida #printa o conteúdo do arquivo "fast.log" de cada linha2 no final do arquivo "saida" 
    done < "$dumps"
done < "$dates"
