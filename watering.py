#import needed libs
import time
from water import water
#define example values
moisMode1 = 0.5
moisMode2 = 0.5
waterTime = 10
def shouldWater(moisture, mode=1, test=False):
    if test: #when in test mode
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
    else: #not in test mode
        if mode==1:
            if moisture>= moisMode2:
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
