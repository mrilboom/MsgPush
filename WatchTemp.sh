#!/bin/bash

while [ true ]; do
    temp=`cat /sys/class/thermal/thermal_zone0/temp`
    if [ ${temp:0:1} = "7" ]; then
        python3 temperature.py ${temp:0:2} 70
        sleep 3600s
    fi
    sleep 5s
done
