#!/bin/bash
for (( ; ; ))
do
   # echo "infinite loops [ hit CTRL+C to stop]"
   python3 /home/pi/src/src_monitoramento_remoto/src_comun_mqtt_modbus_rtu/scan_modbus_to_mqtt_01.py /home/pi/src/src_monitoramento_remoto/src_comun_mqtt_modbus_rtu/local_log1.txt
   sleep 10
done

