### Copyright Fabian L. Blank
### All rights reserved
from sensorread import readDHT, readmoisture
from updatevalues import update
channel_id = "337034"
write_key  = "PDCMJ7FI8E3GRKS5"
def main():
	while True:
		hum, temp = readDHT(2)
		moisture = readmoisture()
		print("#################################")
		print("humidity is ", hum)
		print("temperature is", temp)
		print("moisture is", moisture)
		update(temperature, humidity, moisture, channel_id, write_key)

main()