### Copyright Fabian L. Blank
### All rights reserved

import sys
import Adafruit_DHT
from gpiozero import MCP3008
import statistics as s
import RPi.GPIO as GPIO
import statistics

numOfReads = 10 # Numbers of sensor readings

<<<<<<< HEAD
def readMoisture():
# a part of this code is by modmypi https://github.com/modmypi/Moisture-Sensor/blob/master/moisture.py
	GPIO.setup(channel, GPIO.IN)
	SensorValue = GPIO.input(channel)
	print(SensorValue)
	return 0
def initMoisture():
	# a part of this code is by modmypi https://github.com/modmypi/Moisture-Sensor/blob/master/moisture.py
	# Set our GPIO numbering to BCM
	GPIO.setmode(GPIO.BCM)

	# Define the GPIO pin that we have our digital output from our sensor connected to
	channel = 3
	# Set the GPIO pin to an input
	GPIO.setup(channel, GPIO.IN)

	# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
	GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
	# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
	GPIO.add_event_callback(channel, callback)
def callback(channel):  
	if GPIO.input(channel):
		print "LED off"
		sendEmail(message_dead)
	else:
		print "LED on"
		sendEmail(message_alive)

=======
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
>>>>>>> parent of d577a5c... add support for temperature sensor


def readDHT (pin): 
	#sensorargs = DHT TYPE
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

