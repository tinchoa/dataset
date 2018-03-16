#!/bin/bash

#path=$(pwd)					# variável que assume o valor do diretório atual
path=$1
pathlogs=/usr/local/var/log/suricata		# variável que assume o valor do diretório suricata (guaratiba)
ls $path -1 | grep dump* > $path/new2       # copia o conteudo antes do ">" para o arquivo "new2" dentro do diretório "$PATH"
arquivo=$path/new2				# variável que assume o valor do arquivo atual/new2
#rm new

while read -r line				# loop para ler as linhas do arquivo 
do
	f="$line"				# variável que assume o nome da linha do arquivo
	echo 'analizing file '$f		# o F é maiúsculo mesmo?	
	v2=${f/.}				# Retira o ponto do arquivo pcap para se tornar valor da variável "v2"
	echo "$v2" >> $path/new
	mkdir $path/$v2				# cria um diretório com o valor da variável v2

	# Suricata 4.0.3
	suricata -c /etc/suricata/suricata-2.yaml -r $path/$f -l $path/$v2 -v	# roda o suricata e move os logs para a pasta "v2"

	# Suricata 3.1
	#/root/suricata-3.1/src/suricata -c /usr/local/etc/suricata/suricata-3.yaml -r $path/$f -l $v2 -v	# roda o suricata e move os logs para a pasta "v2"
	
	cp $f $v2				# copia o arquivo com nome da variável f, com nome de v2
	#mv $pathlogs/* $v2			# move os arquivos logs para o diretório v2

done < "$arquivo"				# a variavel line se refere a cada linha da variavel "arquivo" que representa um arquivo
