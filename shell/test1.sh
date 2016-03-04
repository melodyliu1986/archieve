#!/usr/bin/bash

NUM=1
MAX=1000

while [ $NUM -lt $MAX ]
do
    NUM=`expr $NUM + 1`
    echo 'test'
done
