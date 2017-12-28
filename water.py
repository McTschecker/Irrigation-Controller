import time
def water(s):
    from gpiozero import LED
    ##code for watering here
    print("Watering neccesary, Watering now")
    #led on GPIO pin 25
    led = LED(25)
    led.on()
    time.sleep(s)
    led.off()
