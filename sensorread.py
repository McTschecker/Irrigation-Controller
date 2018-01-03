### Copyright Fabian L. Blank
### All rights reserved

import sys
import Adafruit_DHT
from gpiozero import MCP3008
import statistics as s
import RPi.GPIO as GPIO
import statistics

numOfReads = 10 # Numbers of sensor readings

#read the moisture from a Yl-69 over a YL-38 with a MCP3008
def readMoisture():
	pot = MCP3008(0)#specify the MCP3008 port
	moistureA = [pot.value]#read the first value
	for h in range(numOfReads):
		moistureA = moistureA +  [pot.value] #add the reading value to the list of values
	moisture = s.mean(moistureA) #calculate the mean of the list
	return moisture #return the value


def readDHT (pin):
	sensor = Adafruit_DHT.DHT22 #define the Sensor as a DHT22
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) #try to read the sensor
	humidA = [humidity] #list for Humidity
	tempA = [temperature] #list for temperature
	for i in range(numOfReads):
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) #try to read
		humidA = humidA + [humidity] #add the most recent value to the humidity list
		tempA = tempA + [temperature] #add the most recent value to the temperature list
	#mean the values
	humidity = statistics.mean(humidA)
	temperature = statistics.mean(tempA)
	return humidity, temperature #return the values
