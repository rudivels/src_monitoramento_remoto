# Hardware Raspberry PI, placa serial TTL - RS485, Multimedidor Sentron PAC3100
# Rudi van Els @ 29/02/2020
# Programa que implementa Protocolo Modbus e MQTT 

# Programa para ler Multi-Medidor Sentron PAC3100
# Hardware Raspberry Pi com SN75176 e optoisoladores

# Comversor RS485 - proprio com 4n25 e 6n135

# Para habilitar a porta no modo RS485 tem que rodar o programa 
# /home/pi/bin/rpirtscts on

# Interacao com KST-plot
# versao 03/03/2020 reduzindo espacos no publish
#                   versao testado no crontab <ok> com amostragem de a cada minuto
#                   inciar versao para gravar local em disco logfile
#                   renomeado para publish_microhydro_002.py
#                   tirando prints para nao sobrecarregar nohup.out
# Colocar um flag de debug para facilitar a depuracao e tirar os prints
#
# versao 08/03/2020 Preparando leitura de corrente e potencia
#                   Falta checar se a leitura do modbus foi bem sucedida
# versao 23/05/2020 Deixar um flag para sinalizar no dislay lcd que o modbus estah ok
#                   Quando o modbus nao funcionar nao gravar no logdisc...  para nao preencher espaco
#                   importante eh quando faltou comunicacao e quando voltou. 
#
# versao 21/10/2020 Mudanca do diretorios e nomes e mudou para Raspberry pi Zero
#                   mudou de publish_microhydro_002.py para scan_modbus_to_mqtt_01.py
#                   organizou os arquivos com repositorio no github
# versao 22/10/2020 Quando detectar sem comunicacao no modbus manda valores zer para o broker
#                     
# 
import mod_medidor
from datetime import datetime
from random import random 
import paho.mqtt.publish as publish
import time
import sys

if (len(sys.argv))==2 :
	# print ("# logfile  = ", sys.argv[1])
	logfile=True
else :
    logfile=False 

t=str(datetime.now())
agora=t[:19]

# agora="2020-10-22 01:38:36"

####
##   rotina para reduzir o string
##   s = str(agora) 
##   2020-03-03 01:38:36.519665
##   s[:21]
##   2020-03-03 01:38:36.5
##   2020-03-03 01:38:36
####


f2 = open("/home/pi/src/src_monitoramento_remoto/src_comun_mqtt_modbus_rtu/modbuscon.log","w")

if (mod_medidor.testa()==1) :
    f2.write("1\n")
    f2.close()
    publish.single("ChapHydro/rs485", (str(agora)+";"+"1") ,hostname="mqtt.eclipse.org")
    frequencia = round(mod_medidor.leia(39),1)  # frequencia
    publish.single("ChapHydro/frequencia", (str(agora)+";"+str(frequencia)) ,hostname="mqtt.eclipse.org")    
    tensao_A =   round(mod_medidor.leia(1),1)   # tensao 1    
    publish.single("ChapHydro/tensao_A", (str(agora)+";"+str(tensao_A)) ,hostname="mqtt.eclipse.org")        
    tensao_B =   round(mod_medidor.leia(3),1)   # tensao 2
    tensao_C =   round(mod_medidor.leia(5),1)   # tensao 2
    corrente_A  =   round(mod_medidor.leia(13),1)   # tensao 2
    corrente_B  =   round(mod_medidor.leia(15),1)   # tensao 2
    corrente_C  =   round(mod_medidor.leia(17),1)   # tensao 2
    pot_ativa_A =   round(mod_medidor.leia(25),1)   # tensao 2
    pot_ativa_B =   round(mod_medidor.leia(27),1)   # tensao 2
    pot_ativa_C =   round(mod_medidor.leia(29),1)   # tensao 2
    fator_pot   =   round(mod_medidor.leia(53),1)   # tensao 2
    s = str(agora)+";"+str(frequencia)+";"+ str(tensao_A)+";"+str(tensao_B)+";"+str(corrente_A)+";"+str(corrente_B)+";"+str(corrente_C)+";"+str(pot_ativa_A)+";"+str(pot_ativa_B)+";"+str(pot_ativa_B)+";"+str(fator_pot)
    print(s)
    if (logfile == True) :
          f = open(sys.argv[1],"a")
          f.write(s)
          f.write("\n")
          f.close()


else:
    f2.write("0\n")
    f2.close()
    publish.single("ChapHydro/rs485", (str(agora)+";"+"0") ,hostname="mqtt.eclipse.org")
    frequencia = 0 #//round(mod_medidor.leia(39),1)  # frequencia
    publish.single("ChapHydro/frequencia", (str(agora)+";"+str(frequencia)) ,hostname="mqtt.eclipse.org")  
    tensao_A =   0 #//round(mod_medidor.leia(1),1)   # tensao 1
    publish.single("ChapHydro/tensao_A", (str(agora)+";"+str(tensao_A)) ,hostname="mqtt.eclipse.org")  
    tensao_B =   0 #//round(mod_medidor.leia(3),1)   # tensao 2
    tensao_C =   0 #//round(mod_medidor.leia(5),1)   # tensao 2
    corrente_A  =0 #//  round(mod_medidor.leia(13),1)   # tensao 2
    corrente_B  =0 #   round(mod_medidor.leia(15),1)   # tensao 2
    corrente_C  =0 #   round(mod_medidor.leia(17),1)   # tensao 2
    pot_ativa_A =0 #   round(mod_medidor.leia(25),1)   # tensao 2
    pot_ativa_B =0 #    round(mod_medidor.leia(27),1)   # tensao 2
    pot_ativa_C =0 #   round(mod_medidor.leia(29),1)   # tensao 2
    fator_pot   =0 #    round(mod_medidor.leia(53),1)   # tensao 2  
    s = str(agora)+";"+str(frequencia)+";"+ str(tensao_A)+";"+str(tensao_B)+";"+str(corrente_A)+";"+str(corrente_B)+";"+str(corrente_C)+";"+str(pot_ativa_A)+";"+str(pot_ativa_B)+";"+str(pot_ativa_B)+";"+str(fator_pot)
    print("# " + str(agora) + "; Sem modbus 2 ")
    if (logfile == True) :
        f = open(sys.argv[1],"a")
        f.write("# " + str(agora) + "; Sem modbus 3")
        f.write("\n")
        f.close()



f3 = open("/home/pi/src/src_monitoramento_remoto/src_leia_tensoes/rede.log","r")
rede=f3.readline()
f3.close()
publish.single("ChapHydro/Rasp_rede", (str(agora)+";"+ rede) ,hostname="mqtt.eclipse.org") 
   
f3 = open("/home/pi/src/src_monitoramento_remoto/src_leia_tensoes/bateria.log","r")
bateria=f3.readline()
f3.close()
publish.single("ChapHydro/Rasp_bateria", (str(agora)+";"+ bateria) ,hostname="mqtt.eclipse.org") 


# s = str(agora)+";"+str(frequencia)+";"+ str(tensao_A)+";"+str(tensao_B)+";"+str(corrente_A)+";"+str(corrente_B)+";"+str(corrente_C)+";"+str(pot_ativa_A)+";"+str(pot_ativa_B)+";"+str(pot_ativa_B)+";"+str(fator_pot)
#print(s)
#if (logfile == True) :
#    f = open(sys.argv[1],"a")
#    f.write(s)
#    f.write("\n")
#    f.close()

# publish.single("ChapHydro", s ,hostname="mqtt.eclipse.org")
#
# print("Publicou dados ")
