#!/bin/bash

FILES=/home/diogo/170222-dataset/nPPoe
pathlogs=/var/log/snort/alert


a=0
for f in *.pcap*
do
#  v2=${f::-5}
  v2=${f/.}
  echo 'analizing file '$v2
  snort -c /etc/snort/etc/snort.conf -r $f
  mv $pathlogs $v2
done





