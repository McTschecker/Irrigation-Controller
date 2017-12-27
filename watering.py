moisMode1 = 0.5 ###example Values
moisMode2 = 0.75  ####example Values
waterTime = 10
def shouldWater(moisture, mode=1):
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
    ##code for watering here
    print("Watering neccesary, Watering now")
    #led on GPIO pin 25
    