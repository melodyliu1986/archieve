#!/usr/bin/bash

NUM=1
MAX=100

while [ $NUM -lt $MAX ]
do
    NUM=`expr $NUM + 1`
    echo 'test'
done

file="/home/liusong/test.txt"
if [ -f $file ]
then
    echo "The file is a ordinary file, it is not block file or directory!"
else
    echo "The file is block file or directory!"
fi
