#!/bin/bash

if [ $# -ne 3 ] && [ $# -ne 4 ]; then
  echo "Usage: ./setup.sh <channel> <width> <mac> [optional_param]"
  exit 1
fi

channel=$1
width=$2
mac=$3

if [ $# -eq 4 ]; then
  filter=$4
  code=`mcp -c $channel/$width -C 1 -N 1 -m $mac -b $filter`
else
  code=`mcp -c $channel/$width -C 1 -N 1 -m $mac`
fi

sudo ifconfig wlan0 up
sudo nexutil -Iwlan0 -s500 -b -l34 -v$code

sudo iw dev wlan0 interface add mon0 type monitor
sudo ip link set mon0 up

echo "Chanspec confirmation: "
nexutil -k