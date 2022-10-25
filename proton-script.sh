#!/bin/bash

vpn_servers=(IS-IL#1 IL#5 IL#6 IL#7 IL#8 CH-IL#1 IL#9 IL#10 IL#11 IL#12 CY#1 CY#2 CY#3 CY#4 CH-CY#1)
index=$(<index.txt)

protonvpn-cli connect ${vpn_servers[$index]}
index=$((index+1))
if [[ index -eq ${#vpn_servers[@]} ]];
then
  index=0
fi
echo $index > index.txt