### Copyright Fabian L. Blank
### All rights reserved

import sys
import Adafruit_DHT
import Numpy as np
from gpiozero import MCP3008
import statistics as s

numOfReads = 10 # Numbers of sensor readings

def readmoisture():
	pot = MCP3008(0)
	print(pot.value)
	moistureA = [pot.value]
	for h in range(numOfReads):
		print("soil moisture", pot.value)
		moistureA = moistureA +  [pot.value]
	moisture = s.mean(moistureA)
	print("average moisture", moisture)
	return moisture


def readDHT (PinDHT, DHT_TYPE = Adafruit_DHT.DHT.22): 
	#sensorargs = DHT TYPE
	sensor = DHT_TYPE

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	humidA = [humidity]
	tempA = [temperature]
	for i in range(numOfReads):
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		humidA = humidA + [humidity]
		tempA = tempA + [temperature]
	humidity = a.mean(humidA)
	temperature = s.mean(tempA)
	return humidity, temperature
