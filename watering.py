moisMode1 = 0.75 ###example Values
moisMode2 = 0.8  ####example Values
waterTime = 10
def shouldWater(mode=1,moisture):
    if mode==1:
        if moisture>= moisMode1:
            print("Watering neccesary, Watering now")
            water(waterTime)
            return true
        else:
            print("Watering not neccesary")
            return false
    elif mode== 2:
        if moisture>= moisMode2:
            print("Watering neccesary, Watering now")
            water(waterTime)
            return true
        else:
            print("Watering not neccesary")
            return false
    else:
        raise exeption("Unknown Mode, please select an configured mode!")



def water(s):
    ##code for watering here