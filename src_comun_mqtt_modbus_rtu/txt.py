
# 
# import mod_medidor
#from datetime import datetime
#from random import random 
#import paho.mqtt.publish as publish
#import time
#import sys



f3 = open("/home/pi/src/src_monitoramento_remoto/src_leia_tensoes/rede.log","r")
rede=f3.read()
f3.close()
print("rede=")
print(rede)
   
f3 = open("/home/pi/src/src_monitoramento_remoto/src_leia_tensoes/bateria.log","r")
bateria=f3.readline()
f3.close()

print(" bateria ")
print(bateria)

print("Fim")
