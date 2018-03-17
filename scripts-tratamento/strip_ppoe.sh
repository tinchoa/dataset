#!/bin/bash -x

#before running must be created 2 folders 
# nPPoe where the output of the stripe will go
# pass where the file without strip will go

FILES=$1 #passig the file location by argument
pathstrip=/home/stripe
#netAI-rules-stats-ni.xml

for f in $FILES/dump* #atribui o valor da variável "f" a cada arquivo pcap na pasta tmp
do
   file="${f##*/}" # Atribui o valor da variável file ao nome do arquivo "dump.pcapxxx"
   echo 'analizing file '$file
   $pathstrip/stripe -r $f -w $FILES/nPPoe/$file # Remove o PPoE do arquivo dump.pcapxxx e
   mv $FILES/$f $FILES/pass
done                                       #envia o(s) arquivo(s) a pasta com o mesmo nome do                                           #determinado pcap em análise   
