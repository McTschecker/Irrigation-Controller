import time
from gpiozero import LED
def water(s):
    ##code for watering here
    print("Watering neccesary, Watering now")
    #led on GPIO pin 25
    led = LED(25)
    led.on()
    time.sleep(s)
    led.off()
