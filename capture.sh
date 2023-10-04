#!/bin/bash
if [ $# -ne 4 ]
  then
    echo "Usage: ./setup.sh <folderName> <description> <timeSlice> <fileCount>"
    exit 1
fi

folder=$1
description=$2
timeSlice=$3
filecount=$4

# d=`(date '+%Y-%m-%d-%H-%M-%s')`
fname=$folder

rm -rf $fname
mkdir $fname

echo $description > ./$fname/README.md
sudo tcpdump -i wlan0 dst port 5500 -vv -w ./$fname/out.pcap -G $timeSlice -W $filecount

echo "Done"
