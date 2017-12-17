from updatevalues import update
import os
def testUpdateValues():
    temperature = os.urandom(2)
    humidity = os.urandom(6)
    moisture = os.random(256)
    write_key = "ENZIKF2E2KS08KD4"
    channel_id = 386549
    update(temperature, humidity, moisture, channel_id, write_key)
    print("Succesfully put some values to thingspeak")

testUpdateValues()