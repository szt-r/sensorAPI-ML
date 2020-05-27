#!/bin/bash

Get_ip() {
  ip addr | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | grep -v -E "*.*.*.255" | grep -v 127* 
}

IP=`Get_ip | head -1`

echo IP_ADDRESS=$IP > .env
echo PORT=3030 >> .env
