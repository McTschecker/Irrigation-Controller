from updatevalues import update
import os
def testUpdateValues():
    temperature = 1000
    humidity = -10
    moisture = 100000
    write_key = "ENZIKF2E2KS08KD4"
    channel_id = 386549
    update(temperature, humidity, moisture, channel_id, write_key)
    print("Succesfully put some values to thingspeak")

testUpdateValues()