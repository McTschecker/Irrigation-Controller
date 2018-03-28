### Copyright Fabian L. Blank
### All rights reserved
from sensorread import readDHT, readMoisture
from updatevalues import update
import pigpio
import time
from watering import shouldWater
waitingTime = 1440 #Time waiting in seconds
#pigpio.start('soft', 8888)

#####################################################################
# Controls which functions are active
tempHumActive = False
moistureActive = True
publishActive = True
waterActive = True
waitingActive = False

channel_id = "337034"
write_key  = "PDCMJ7FI8E3GRKS5"
def main():
	while True: #run the following code all the time
		print("#################################") #making it easier to read the logs
		#meassuring the temperature
		if(tempHumActive):
			hum, temp = readDHT(2)
			print("temperature is", temp)
			print("humidity is ", hum)
		else:
			print("Temperature and humidity sensor is disabled")
		#read Moisture
		if moistureActive:
			moisture = readMoisture()
			print("moisture is", moisture)
		else:
			print("Moisture sensor is disabled")
		#Send all the Data to thingspeak
		if publishActive:
			update(temp, hum, moisture, channel_id, write_key)
		else:
			print("Publishing to thingspeak is disabled")
		if waterActive:
			shouldWater(moisture)
		else:
			print("Watering is disabled")
		#delay
		if waitingActive:
			print("Waiting", waitingTime, "Seconds")
			time.sleep(waitingTime)
		else:
			print("Waiting is disabled")
main()
