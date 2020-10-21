# Rotinas para implementar o monitoramento remoto num Raspberry Zero

rudi@ 20/10/2020
 
- 1. Programa monitor (linguagem C)
- 2. Programa para ler a tensão de alimentação do Rasp Zero (Liguagem C)
- 3. Programa para comunicação Mqtt e Modbus-RTU (Pyhton)

Sincronizado com o codigo no Raspberry

- Pasta local /home/pi/src/src\_monitoramento\_remoto
- Pasta local /Users/rudi/src/src\_monitoramento\_remoto 
- [Pasta remota githib.com/rudivels](https://github.com/rudivels/src_monitoramento_remoto)

## 1. Programa monitor
Programa implementado em linguagem C que gerencia a rede WiFi, monitora a rede internet, as tensões da bateria e da rede, monitora a rede MODBUS-RTU e MQTT, mostra os dados no display LCD e provê uma interface simples com o usuário por meio de 3 teclas.

Entradas
 
- arquivo `rede.log`
- arquivo `bateria.log`
- arquivo `modbuscon.log`
- arquivo `mqttcon.log`

## 2. Programa para ler a tensão de alimentação do Raspberry Zero

Um script no shell `loop_tensoes.sh` a cada segundo chama um  programa compilado em C `le_bateria` para ler a tensão da bateria e gravar o valor no arquivo `bateria.log`  e em seguido um outro programas compilado em C `le_rede` para ler a tensão da rede e graver o valor em `rede.log`

Optou-se em usar o programa compilado em C para padronizar o acesso ao hardware GPIO do Raspberry e permitir fácil portabilidade.
Os programas usam somente funções padrões das bibiotecas standard do C e o acesso ao GPIO é feito por system call.
Os programas compilador tem como saída o terminal.

O sript fica num loop e tem uma temporização por meio de um `sleep(1)`

entradas 

- escrita no terminal do programa `le_rede`
- escrita no terminal do programa `le_bateria`

saídas

- arquivo `bateria.log`
- arquivo `rede.log`


 
## 3. Programa de comunicação MQTT e MODBUS-RTU

## 3.1. script em shell

A cada 10 segundo o script `loop_publish.sh` chama a rotina em python 3 `scan_modbus_publish_mqtt_01.py`  e escreve os valores obtidos com time stamp num arquivo texo local `local_log1.txt`.

O sript fica num loop e tem uma temporização por meio de um sleep(10)

entrada

- escrita no terminal da rotina  `scan_modbus_publish_mqtt_01.py` em python

saídas

- arquivo `local_log1.txt`

## 3.2. Rotina em python

A rotina `scan_modbus_publish_mqtt_01.py` le os valores do multimedidor pela protocolo MODBUS-RTU e manda via MQTT os dados com time stamp para topic Chapberry no brooker [mqtt.eclipse.org](mqtt.eclipse.org)

Entrada
 
- mod_medidor.py (rotinas para acessar a porta RS485)
- estado da rede TCP/IP (a implementar)

saídas

- arquivo `modbuscon.log`
- arquivo `mqttcon.log` (a implementar)
- escreve no terminal
- mande dados para mqtt.eclipse.org / Chaphydro

