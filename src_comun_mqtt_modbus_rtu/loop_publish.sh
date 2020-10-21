#!/bin/bash
for (( ; ; ))
do
   # echo "infinite loops [ hit CTRL+C to stop]"
   python3 /home/pi/src/src_monitoramento_remoto/src_comun_mqtt_modbus_rtu/publish_microhydro_002.py /home/pi/src/src_monitoramento_remoto/src_comun_mqtt_modbus_rtu/local_log1.txt
   sleep 10
done

