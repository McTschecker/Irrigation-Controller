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
# a part of this code is by modmypi https://github.com/modmypi/Moisture-Sensor/blob/master/moisture.py

	# Define the GPIO pin that we have our digital output from our sensor connected to
	channel = 3
	# Set the GPIO pin to an input
	GPIO.setup(channel, GPIO.IN)
	SensorValue = GPIO.input(channel)
	print(SensorValue)
	return 0



def readDHT (pin): 
	#sensorargs = DHT TYPE
	sensor = Adafruit_DHT.DHT22

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	humidA = [humidity]
	tempA = [temperature]
	for i in range(numOfReads):
		print("reading Temperature", i + 1)
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		print("Humidity is:", humidity)
		print("Temperature is", temperature)
		humidA = humidA + [humidity]
		tempA = tempA + [temperature]
	humidity = statistics.mean(humidA)
	temperature = statistics.mean(tempA)
	return humidity, temperature

