### Copyright Fabian L. Blank
### All rights reserved
from sensorread import readDHT, readMoisture
from updatevalues import update
import pigpio
import time
from watering import shouldWater
waitingTime = 60 #Time waiting in seconds
#pigpio.start('soft', 8888)
channel_id = "337034"
write_key  = "PDCMJ7FI8E3GRKS5"
def main():
	while True:
		hum, temp = readDHT(2)
		moisture = readMoisture()
		print("#################################")
		print("humidity is ", hum)
		print("temperature is", temp)
		print("moisture is", moisture)
		update(temp, hum, moisture, channel_id, write_key)
		shouldWater(moisture)
		#delay
		print("Waiting", waitingTime, 'Seconds')
		time.sleep(waitingTime)
main()