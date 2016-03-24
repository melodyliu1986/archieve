#!/usr/bin/env bash
echo "Please input three numbers"
read -p "please input the first number: " n1
read -p "please input the second number: " n2
read -p "please input the third number: " n3

max(){
tmp=$1
if [ $tmp -le $2 ]
then
    tmp=$2
fi
if [ $tmp -le $3 ]
then
    tmp=$3
fi
echo "The max number is: $tmp"
}

max $n1 $n2 $n3




