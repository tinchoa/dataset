#!/bin/bash -x

FILES=/tmp
pathstrip=/home/airam/stripe
#netAI-rules-stats-ni.xml

for f in $FILES/dump.pcap* #atribui o valor da variável "f" a cada arquivo pcap na pasta tmp
do
   file="${f##*/}" # Atribui o valor da variável file ao nome do arquivo "dump.pcapxxx"
   echo 'analizing file '$file
   $pathstrip/stripe -r $f -w $(pwd)/$file # Remove o PPoE do arquivo dump.pcapxxx e
done                                       #envia o(s) arquivo(s) a pasta com o mesmo nome do                                           #determinado pcap em análise   
