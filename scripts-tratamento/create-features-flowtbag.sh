#!/bin/bash

path=$(pwd)
arquivo=$path/folders
saida=$path/features.out

while read -r line
do
        f="$line"
        a="$(ls $f |grep pcap)"
        echo 'analizing file '$a
        # mkdir $v2
        echo $path'/'$f'/'$a
        flowtbag $path'/'$f'/'$a  > /tmp/24/flowtbag.out
        cat /tmp/24/flowtbag.out >>$saida

 done < "$arquivo"



