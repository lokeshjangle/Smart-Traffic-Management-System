import threading
import time
import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices [1].id)
def engine_talk(text):
	engine.say(text)
	engine.runAndWait()
def set_rotation(count_r1,count_r2,count_r3,count_r4):
        if count_r1 == 0 and count_r2!=0 and count_r3!=0 and count_r4!=0:
                        #Route_2.capture()
                        #Route_2.ExtractImage()
                        count_r1 = 0
                        count_r2 = int(input("c2:"))
                        #Route_3.capture()
                        #Route_3.ExtractImage()
                        count_r3 = int(input("c3:"))
                        #Route_4.capture()
                        #Route_4.ExtractImage()
                        count_r4 = int(input("c4:"))
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r2 == 0 and count_r1!=0 and count_r3!=0 and count_r4!=0:
                        #Route_1.capture()
                       # Route_1.ExtractImage()
                        count_r1 = int(input("c1:"))
                        #Route_3.capture()
                        #Route_3.ExtractImage()
                        count_r2=0
                        count_r3 = int(input("c3:"))
                       # Route_4.capture()
                        #Route_4.ExtractImage()
                        count_r4 = int(input("c4:"))
                        return setRoute(count_r1,count_r2, count_r3, count_r4)

        elif count_r3 == 0 and count_r1!=0 and count_r2!=0 and count_r4!=0:
                       # Route_1.capture()
                       # Route_1.ExtractImage()
                        count_r1 = int(input("R1:"))
                       # Route_2.capture()
                       # Route_2.ExtractImage()
                        count_r2 = int(input("R2:"))
                       # Route_4.capture()
                        #Route_4.ExtractImage()
                        count_r3=0
                        count_r4 = int(input("R4:"))
                        return setRoute(count_r1, count_r2,count_r3, count_r4)

        elif count_r4 == 0 and count_r1!=0 and count_r2!=0 and count_r3!=0:
                        #Route_1.capture()
                       # Route_1.ExtractImage()
                        count_r1 = int(input("R1:"))
                       # Route_2.capture()
                       # Route_2.ExtractImage()
                        count_r2 = int(input("R2:"))
                        #Route_3.capture()
                       # Route_3.ExtractImage()
                        count_r3 = int(input("R3:"))
                        count_r4 = 0
                        return setRoute(count_r1, count_r2, count_r3, count_r4)

        elif count_r1 == 0 and count_r2 == 0 and count_r3!=0 and count_r4!=0:
                        #Route_3.capture()
                        #Route_3.ExtractImage()
                        count_r1 = 0
                        count_r2 = 0
                        count_r3 = int(input("R3:"))
                        #Route_4.capture()
                        #Route_4.ExtractImage()
                        count_r4 = int(input("R4:"))
                        return setRoute(count_r1,count_r2, count_r3, count_r4)

        elif count_r1 == 0 and count_r3 == 0 and count_r2!=0 and count_r4!=0:
                       # Route_2.capture()
                        #Route_2.ExtractImage()
                        count_r1 = 0
                        count_r2 = int(input("R2:"))
                       # Route_4.capture()
                       # Route_4.ExtractImage()
                        count_r3 = 0
                        count_r4 = int(input("R4:"))
                        return setRoute(count_r1, count_r2,count_r3, count_r4)
        elif count_r1 == 0 and count_r4 == 0 and count_r2!=0 and count_r3!=0:
                        #Route_2.capture()
                        #Route_2.ExtractImage()
                        count_r1 = 0
                        count_r2 = int(input("R2:"))
                        #Route_3.capture()
                        #Route_3.ExtractImage()
                        count_r3 = int(input("R3:"))
                        count_r4=0
                        return setRoute(count_r1, count_r2, count_r3,count_r4)
        elif count_r2 == 0 and count_r3 == 0 and count_r1!=0 and count_r4!=0:
                        #Route_1.capture()
                        #Route_1.ExtractImage()
                        count_r1 = int(input("R1:"))
                        count_r2 = 0
                        count_r3 = 0
                        #Route_4.capture()
                       # Route_4.ExtractImage()
                        count_r4 = int(input("R4:"))
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        
        elif count_r2 == 0 and count_r4 == 0 and count_r1!=0 and count_r3!=0:
                        #Route_1.capture()
                       # Route_1.ExtractImage()
                        count_r1 = int(input("R1:"))
                        count_r2 = 0
                        #Route_3.capture()
                        #Route_3.ExtractImage()
                        count_r3 = int(input("R3:"))
                        count_r4 = 0
                        return setRoute(count_r1,count_r2, count_r3,count_r4)
        
        elif count_r3 == 0 and count_r4 == 0 and count_r1!=0 and count_r2!=0:
                        #Route_1.capture()
                       # Route_1.ExtractImage()
                        count_r1 = int(input("R1:"))
                        #Route_2.capture()
                       # Route_2.ExtractImage()
                        count_r2 = int(input("R2:"))
                        count_r3 = 0
                        count_r4 = 0
                        return setRoute(count_r1, count_r2,count_r3, count_r4)
        
        elif count_r1 != 0 and count_r2 == 0 and count_r3 == 0 and count_r4==0:
                        #Route_1.capture()
                        #Route_1.ExtractImage()
                        count_r1 = int(input("R1:"))
                        count_r2 = 0
                        count_r3 = 0
                        count_r4 = 0
                        return setRoute(count_r1, count_r2,count_r3, count_r4)
        elif count_r1 == 0 and count_r2 != 0 and count_r3 == 0 and count_r4==0:
                       # Route_2.capture()
                        #Route_2.ExtractImage()
                        count_r1 = 0
                        count_r2 = int(input("R2:"))
                        count_r3 = 0
                        count_r4 = 0
                        return setRoute(count_r1, count_r2,count_r3, count_r4)
        elif count_r1 == 0 and count_r2 == 0 and count_r3 != 0 and count_r4!=0:
                        #Route_3.capture()
                        #Route_3.ExtractImage()
                        count_r1 = 0
                        count_r2 = 0
                        count_r3 = int(input("R3:"))
                        count_r4 = 0
                        return setRoute(count_r1, count_r2,count_r3, count_r4)
        elif count_r1 == 0 and count_r2 == 0 and count_r3 == 0 and count_r4!=0:
                       # Route_4.capture()
                       # Route_4.ExtractImage()
                        count_r2 = 0
                        count_r3 = 0
                        count_r4 = 0
                        count_r4 = int(input("R4:"))
                        return setRoute(count_r1, count_r2,count_r3,count_r4)
        elif count_r1 == 0 and count_r2 == 0 and count_r3 == 0 and count_r4 == 0:
                        exit()
                

 
def setRoute(count_r1,count_r2,count_r3,count_r4):
        # set_rotation(count_r1, count_r2, count_r3, count_r4)

        # set_rotation(count_r1, count_r2, count_r3, count_r4)
        print(count_r1)
        print(count_r2)
        print(count_r3)
        print(count_r4)
        if count_r1>count_r2 and count_r1>count_r3 and count_r1 > count_r4:
                print("Release Route 1")
                engine_talk("Release Route 1")
                count_r1 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)
        elif count_r2>count_r1 and count_r2>count_r3 and count_r2 > count_r4:
                print("Release Route 2")
                engine_talk("Release Route 2")
                count_r2 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)
        elif count_r3>count_r1 and count_r3>count_r2 and count_r3 > count_r4:
                print("Release Route 3")
                engine_talk("Release Route 3")
                count_r3 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)
        elif count_r4>count_r1 and count_r4>count_r2 and count_r4 > count_r3:
                print("Release Route 4")
                engine_talk("Release Route 4")
                count_r4 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)

        
count_r1 = int(input("R1:"))
count_r2 = int(input("R2:"))
count_r3 = int(input("R3:"))
count_r4 = int(input("R4:"))
setRoute(count_r1, count_r2, count_r3, count_r4)
# set_rotation(count_r1, count_r2, count_r3, count_r4)