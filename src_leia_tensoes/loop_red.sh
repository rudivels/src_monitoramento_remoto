#!/bin/bash 
for (( ; ; ))
do
   /home/pi/src/src_monitoramento_remoto/src_leia_tensoes/le_rede > /home/pi/src/src_monitoramento_remoto/src_leia_tensoes/rede.log
   sleep 1
done 
