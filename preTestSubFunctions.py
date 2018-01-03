from updatevalues import update
import random
from watering import shouldWater
def testUpdateValues():
    #create random values
    temperature = random.randint(0,500)
    humidity = random.randint(0,100)
    moisture = random.randint(0,10000)
    #needed keys for thingspeak
    write_key = "ENZIKF2E2KS08KD4"
    channel_id = 386549
    #publish the random values
    update(temperature, humidity, moisture, channel_id, write_key)
    print("Succesfully put some values to thingspeak")

#run the test for updates
testUpdateValues()
