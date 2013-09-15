#!/usr/bin/python

#Código Python para exibir num visor LCD o nº IP e a temperatura da CPU
#Adicionar ainda sistema de segurança no Raspberry Pi, nesse mesmo código, ao ler a temperatura, se ela for igual ou maior que 70.0° C, desligar o Pi.
#Código abaixo ainda está como o da Adafruit, mostrando apenas IP e Hora Atual, verificar o tempo de atualização

from CharLCD import CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = CharLCD

cmd1 = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
#cmd2 = "vcgencmd measure_temp | cut -d "=" -f2 | cut -d "'" -f1"

lcd.begin(16,1)

def run_cmd1(cmd1):
	  p = Popen(cmd1, shell=True, stdout=PIPE)
	  output = p.communicate()[0]
	  return output

#def run_cmd1(cmd1):
	  #p = Popen(cmd1, shell=True, stdout=PIPE)
	  #output = p.communicate()[0]
	  #return output


while 1:
	lcd.clear()
	ipaddr = run_cmd1(cmd1)
	#temp = run_cmd2(cmd2)
	lcd.message(datetime.now()strftime('%b %d %H:%M:%S\n'))
	lcd.message('IP %s' % (ipaddr))
	#lcd.message('Temp. %s' % (temp))
	sleep(2)
