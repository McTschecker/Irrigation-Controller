

import sys
import Adafruit_DHT
import Numpy as np

numOfReads = 10 # Numbers of sensor readings
#increase nom of reads by one to get it running the specific times
numOfReads = numOfReads +1

def readDHT(PinDHT, DHT_TYPE=Adafruit_DHT.DHT.22): #sensorargs = DHT TYPE
	sensor = DHT_TYPE

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	humidA = np.Array(humidity)
	tempA = np.Array(temperature)
	for i in range(numOfReads):
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		humidA = np.append(humidA, humidity)
		tempA = np.append(tempA, temperatur)
	humidity = np.mean(humidA)
	temperature = np.mean(tempA)
	return humidity, temperature
