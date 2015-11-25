#!/bin/bash
cd `pwd`


for i in `ls *_sc`
do
   python ../dealresult.py -f1 $i.txt -f2 $i
done





if [ ! -f "$1" ];then
  echo "no file named $1"
  touch "$1"
else
 echo "had the file named $1 next step remove it and rebulid it"
 rm "$1"
 touch "$1"
fi



for i in `ls *sc.txt`
do 

  python ../dealallresult.py -f1 $i -O $1
done 
