### Copyright Fabian L. Blank
### All rights reserved
from sensorread import readDHT
def main():
	while True:
		hum, temp = readDHT()
		print("#################################")
		print("humidity is ", hum)
		print("temperature is", temp)
main()