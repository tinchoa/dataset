#!/bin/bash

FILES=/home/diogo/170222-dataset
pathstrip=/home/diogo/stripe/
#netAI-rules-stats-ni.xml


for f in *.pcap*
do
   echo 'analizing file '$f
   $pathstrip/stripe -r $f -w $FILES/nPPoe/$f
done
