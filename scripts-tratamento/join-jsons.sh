#!/bin/bash

arquivo=/home/dataset-Renato/folders.txt
saida=/home/dataset-Renato/json-all.txt


while read -r line
do
    f="$line"
    cat $f/eve-test.json >>$saida
    echo 'entering folder '$f
 done < "$arquivo"



