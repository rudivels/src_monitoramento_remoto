#!/bin/bash 
for (( ; ; ))
do
   /home/pi/src/src_monitoramento_remoto/leia_tensoes/le_rede > /home/pi/src/src_monitoramento_remoto/leia_tensoes/rede.log 
   /home/pi/src/src_monitoramento_remoto/leia_tensoes/le_bateria > /home/pi/src/src_monitoramento_remoto/leia_tensoes/bateria.log 
   sleep 1
done 
