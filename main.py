### Copyright Fabian L. Blank
### All rights reserved
from sensorread import readDHT, readmoisture
from updatevalues import update
def main():
	while True:
		hum, temp = readDHT(22)
		moisture = readmoisture()
		print("#################################")
		print("humidity is ", hum)
		print("temperature is", temp)
		print("moisture is", moisture)
		update(temperature, humidity, moisture)

main()