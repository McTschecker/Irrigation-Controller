### Copyright Fabian L. Blank
### All rights reserved
import Adafruit_DHT
print (Adafruit_DHT.DHT.22)
from sensorread import readDHT, readmoisture
from updatevalues import update
def main():
	while True:
		hum, temp = readDHT()
		moisture = readmoisture()
		print("#################################")
		print("humidity is ", hum)
		print("temperature is", temp)
		print("moisture is", moisture)
		update(temperature, humidity, moisture)

main()