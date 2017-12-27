from watering import shouldWater
import time.sleep
def testWatering():
    #Test1 mode 1; value 0.6  ====> True
    test1 = shouldWater(0.6) 
    if test1:
        print("Test 1 passed for watering")
    else:
        raise Exception ("Test 1 failed for vlue of 0.49, should be true in mode 1", test1)
    #Test2 mode 1; value 0.49  ====> False
    test2 = shouldWater(0.49)
    if test2:
         raise Exception ("Test 1 failed for vlue of 0.6, should be false in mode 1", test2)
    else: 
        print("Test 2 passed for watering")
    ###############################################################
    ###mode 2
    print("Now testing mode 2")
    #Test3 mode 2; value 0.9  ====> True
    test1 = shouldWater(0.9, mode=2) 
    if test1:
        print("Test 1 passed for watering")
    else:
        raise Exception ("Test 3 failed for vlue of 0.4, should be true in mode 2", test1)
    #Test2 mode 2; value 0.4  ====> False
    test4 = shouldWater(0.4,mode=2)
    if test2:
         raise Exception ("Test 1 failed for vlue of 0.0, should be false in mode 2", test2)
    else: 
        print("Test 4 passed for watering")
testWatering()