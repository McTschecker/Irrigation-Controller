import time
moisMode1 = 0.5 ###example Values
moisMode2 = 0.75  ####example Values
waterTime = 10
def shouldWater(moisture, mode=1, test=False):
    if test:
        if mode==1:
            if moisture>= moisMode1:
                print("Watering neccesary, Watering now")
                return True
            else:
                print("Watering not neccesary") 
                return False
        elif mode== 2:
            if moisture>= moisMode2:
                print("Watering neccesary, Watering now")
                return True
            else:
                print("Watering not neccesary")
                return False
        else:
            raise exeption("Unknown Mode, please select an configured mode!")
    else:
        if mode==1:
            if moisture>= moisMode1:
                water(waterTime)
                return True
            else:
                print("Watering not neccesary") 
                return False
        elif mode== 2:
            if moisture>= moisMode2:
                water(waterTime)
                return True
            else:
                print("Watering not neccesary")
                return False
        else:
            raise exeption("Unknown Mode, please select an configured mode!")



def water(s):
    #from gpiozero import LED
    ##code for watering here
    print("Watering neccesary, Watering now")
    #led on GPIO pin 25
    # led = LED(25)
    # led.on()
    # time.sleep(waterTime, pin_factory=factory)
    # led.off()
