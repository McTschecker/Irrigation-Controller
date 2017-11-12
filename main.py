### Copyright Fabian L. Blank
### All rights reserved
from subsystems.sensorread import readDHT, readmoisture
from subsystems.updatevalues import update
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