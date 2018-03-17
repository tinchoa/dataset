#!/bin/bash

#create-features-flowtbag.sh abstrai os pcaps em 40 features

path=$1
dates=$path/date-folders.txt

while read -r line1 #A cada loop, atribui o valor de cada data no arquivo "dates"a variável line1
do
    f="$line1" #atribui as datas a variável "f"
    dumps=$path/$f/dump-folders.txt
    saida=$path/$f/features.out
    echo 'entering folder '$f
    while read -r line2 #A cada loop, atribui o valor de cada pcap a variavel line2
    do
	    g="$line2"
	    echo '----entering folder '$g
	    pcap="$(ls $path/$f/$g | grep pcap)" # retorna o nome do pcap que será analisado
	    echo '--------analyzing file '$pcap
	    echo '--------analyzing file '$pcap >$path/log-flowtbag.txt
	    flowtbag $path'/'$f'/'$g'/'$pcap > /tmp/flowtbag.out #comando que abstrai os pcaps em 40 feactures e apresenta um arquivo csv como saída
	    cat /tmp/flowtbag.out >> $saida #escreve o arquivo csv num arquivo de saída que contem todos os outros arquivos csv com a mesma data dos pcaps
    done < "$dumps"
done < "$dates"
