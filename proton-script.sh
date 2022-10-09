#!/bin/bash

israel=true

while true
do
  if $israel; then
    protonvpn-cli connect CH-CY#1
    israel=false
  else
    protonvpn-cli connect IS-IL#1
    israel=true
  fi
  sleep 7
done
