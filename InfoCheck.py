#!/usr/bin/python
#-*- coding: iso-8859-15 -*-

# Código Python para exibir num visor LCD o nº IP e a temperatura da CPU
# Adicionar ainda sistema de segurança no Raspberry Pi, nesse mesmo código, ao ler a temperatura, se ela for igual ou maior que 70.0° C, desligar o Pi.

from CharLCD import CharLCD
from subprocess import *
from time import sleep
import os, serial, commands # importa bibliotecas necessárias para conexão c/ Arduino

lcd = CharLCD
porta = '/dev/ttyACM0' # define a porta de conexão c/ Arduino

cmd1 = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd2 = 'vcgencmd measure_temp | cut -d "=" -f2'

lcd.begin(16,1)

def run_cmd1(cmd1):
	  p = Popen(cmd1, shell=True, stdout=PIPE)
	  output = p.communicate()[0]
	  return output

def run_cmd2(cmd2):
	  p = Popen(cmd2, shell=True, stdout=PIPE)
	  output2 = p.communicate()[0]
	  return output2

while 1:
	lcd.clear()
	ipaddr = run_cmd1(cmd1)
	temp = run_cmd2(cmd2)
	lcd.message('IP %s' % (ipaddr))
	lcd.message('Temp. %s' % (temp))
	sleep(10)

while (True):
	arduino = serial.Serial (porta, 9600) # cria objeto Arduino e conecta ele na porta 9600(/dev/ttyACM0)
	
	valor = commands.getoutput("free | grep Mem | awk '{print $3}'") # armazena o valor do comando "Free" do Linux dentro da variável valor
	
	if(valor <= 83163):
		arduino.write('1')
	elif(valor >= 83163 and <= 166325):
		arduino.write('2')
	elif(valor >= 166326):
		arduino.write('3')
	



 
