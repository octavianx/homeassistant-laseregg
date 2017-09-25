#!/bin/bash
#通过bash 方式获取 Laser Egg 信息的， 需要安装 jq包
# https://gongm.in/2017/01/laser-egg-air-quality-monitor/
# Laser Egg AQI Script
# Original author: i@gongm.in
#
# Usage: aqi <Laser Egg ID>
ID=$1
AlertLevel=21 #AQI=70

if [ "$1" = "" ]; then
        echo "Usage: `basename $0` <Laser Egg ID>"
else
        CMD="http://api-ios.origins-china.cn:8080/topdata/getTopDetail?id=$ID"
        PM25=$(curl -s $CMD | jq -r ".pm2_5")
fi

echo "Laser Egg $ID PM 2.5 reads: [$PM25]."

if ((PM25 > AlertLevel)); then
        echo "Alert!"
        bash ./wemo.sh YOUR_WEMO_IP_ADDRESS_HERE ON
else
        echo "OK"
        bash ./wemo.sh YOUR_WEMO_IP_ADDRESS_HERE OFF
fi

bash 

