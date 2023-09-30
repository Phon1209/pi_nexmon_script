#!/bin/bash

if [ $# -ne 3 ]
  then 
    echo "Usage: ./setup.sh <channel> <width> <mac>"
    exit 1
fi

channel=$1
width=$2
mac=$3

code=`mcp -c $channel/$width -C 1 -N 1 -m $mac`

sudo ifconfig wlan0 up
sudo nexutil -Iwlan0 -s500 -b -l34 -v$code

sudo iw dev wlan0 interface add mon0 type monitor
sudo ip link set mon0 up

echo "Chanspec confirmation: "
nexutil -k