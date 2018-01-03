### Copyright Fabian L. Blank
### All rights reserved

import sys
import Adafruit_DHT
from gpiozero import MCP3008
import statistics as s
import RPi.GPIO as GPIO
import statistics

numOfReads = 10 # Numbers of sensor readings

def readMoisture():
	pot = MCP3008(0)
	moistureA = [pot.value]
	for h in range(numOfReads):
		moistureA = moistureA +  [pot.value]
	moisture = s.mean(moistureA)
	print("average moisture", moisture)
	return moisture


def readDHT (pin):
	sensor = Adafruit_DHT.DHT22
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	humidA = [humidity]
	tempA = [temperature]
	for i in range(numOfReads):
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		humidA = humidA + [humidity]
		tempA = tempA + [temperature]
	humidity = statistics.mean(humidA)
	temperature = statistics.mean(tempA)
	return humidity, temperature
