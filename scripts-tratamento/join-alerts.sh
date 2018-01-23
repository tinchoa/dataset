#!/bin/bash

arquivo=/home/dataset-Renato/folders.txt
saida=/home/dataset-Renato/alertas-all.txt


while read -r line
do
    f="$line"
    cat $f/fast.log >>$saida
    echo 'entering folder $f'
 done < "$arquivo"
