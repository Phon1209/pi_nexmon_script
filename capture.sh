#!/bin/bash

echo $#
if [$# -ne 4]
  then
    echo "Usage: ./setup.sh <folderName> <description> <timeSlice> <totalCaptureTime>"
    exit 1
fi

folder=$1
description=$2
slice=$3
total=$4

d=`(date '+%Y-%m-%d-%H-%M-%s')`
fname=$folder-$d

rm -rf $fname
mkdir $fname

sudo tcpdump -i wlan0 dst port 5500 -vv -w ./$fname/out.pcap

echo "Done"
