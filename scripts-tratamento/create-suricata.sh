#!/bin/bash

path=$(pwd)
pathlogs=/usr/local/var/log/suricata
arquivo=$path/new2

while read -r line
do
        f="$line"
        echo 'analizing file '$f
        v2=${f/.}
        mkdir $v2
        suricata -c /usr/local/etc/suricata/suricata.yaml -r $f -l $v2
        cp $f $v2
#       mv $pathlogs/* $v2

done < "$arquivo"
