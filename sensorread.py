

import sys
import Adafruit_DHT
import Numpy as np

# class temperatur:
# 	pin = 0
# 	def defpin(pini):
# 		pin = pini

# 	def getTemperature():
# 		temperatur = []
		
# 		return temperatur
# 	def getHumidity():
# 		#
# 	def getAll():

def readDHT(PinDHT, DHT_TYPE=Adafruit_DHT.DHT.22): #sensorargs = DHT TYPE
	sensor = DHT_TYPE

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	humidA = np.Array(humidity)
	tempA = np.Array(temperature)
	for i in range(10):
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		humidA = np.append(humidA, humidity)
		tempA = np.append(tempA, temperatur)
	humidity = np.mean(humidA)
	temperature = np.mean(tempA)
	return humidity, temperature
