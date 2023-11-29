import threading
import time
import os
import pyttsx3
from route_1 import Route_1
from route_2 import Route_2
from route_3 import Route_3
from route_4 import Route_4

# import the time module
import time

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
                

# input time in seconds

# function call


engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices [1].id)
def engine_talk(text):
	engine.say(text)
	engine.runAndWait()

# count_r1 = Route_1.vehicles_folder_count_1
# count_r2 = Route_2.vehicles_folder_count_2
# count_r3 = Route_3.vehicles_folder_count_3
# count_r4 = Route_4.vehicles_folder_count_4

def set_rotation(count_r1,count_r2,count_r3,count_r4):
        if count_r1 == 0 and count_r2!=0 and count_r3!=0 and count_r4!=0:
                        count_r1 = 0
                        Route_2.capture()
                        Route_2.ExtractImage()
                        count_r2 = Route_2.vehicles_folder_count_2
                        Route_3.capture()
                        Route_3.ExtractImage()
                        count_r3 = Route_3.vehicles_folder_count_3
                        Route_4.capture()
                        Route_4.ExtractImage()
                        count_r4 = Route_4.vehicles_folder_count_4
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r2 == 0 and count_r1!=0 and count_r3!=0 and count_r4!=0:
                        Route_1.capture()
                        Route_1.ExtractImage()
                        count_r1 = Route_1.vehicles_folder_count_1
                        count_r2 = 0
                        Route_3.capture()
                        Route_3.ExtractImage()
                        count_r3 = Route_3.vehicles_folder_count_3
                        Route_4.capture()
                        Route_4.ExtractImage()
                        count_r4 = Route_4.vehicles_folder_count_4
                        return setRoute(count_r1, count_r2, count_r3, count_r4)

        elif count_r3 == 0 and count_r1!=0 and count_r2!=0 and count_r4!=0:
                        Route_1.capture()
                        Route_1.ExtractImage()
                        count_r1 = Route_1.vehicles_folder_count_1
                        Route_2.capture()
                        Route_2.ExtractImage()
                        count_r2 = Route_2.vehicles_folder_count_2
                        count_r3 = 0
                        Route_4.capture()
                        Route_4.ExtractImage()
                        count_r4 = Route_4.vehicles_folder_count_4
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r4 == 0 and count_r1!=0 and count_r2!=0 and count_r3!=0:
                        Route_1.capture()
                        Route_1.ExtractImage()
                        count_r1 = Route_1.vehicles_folder_count_1
                        Route_2.capture()
                        Route_2.ExtractImage()
                        count_r2 = Route_2.vehicles_folder_count_2
                        Route_3.capture()
                        Route_3.ExtractImage()
                        count_r3 = Route_3.vehicles_folder_count_3
                        count_r4 = 0
                        return setRoute(count_r1, count_r2, count_r3, count_r4)

        elif count_r1 == 0 and count_r2 == 0 and count_r3!=0 and count_r4!=0:
                        count_r1 = 0
                        count_r2 = 0
                        Route_3.capture()
                        Route_3.ExtractImage()
                        count_r3 = Route_3.vehicles_folder_count_3
                        Route_4.capture()
                        Route_4.ExtractImage()
                        count_r4 = Route_4.vehicles_folder_count_4
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r1 == 0 and count_r3 == 0 and count_r2!=0 and count_r4!=0:
                        count_r1 = 0
                        Route_2.capture()
                        Route_2.ExtractImage()
                        count_r2 = Route_2.vehicles_folder_count_2
                        count_r3 = 0
                        Route_4.capture()
                        Route_4.ExtractImage()
                        count_r4 = Route_4.vehicles_folder_count_4
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r1 == 0 and count_r4 == 0 and count_r2!=0 and count_r3!=0:
                        count_r1 = 0
                        Route_2.capture()
                        Route_2.ExtractImage()
                        count_r2 = Route_2.vehicles_folder_count_2
                        Route_3.capture()
                        Route_3.ExtractImage()
                        count_r3 = Route_3.vehicles_folder_count_3
                        count_r4 = 0
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r2 == 0 and count_r3 == 0 and count_r1!=0 and count_r4!=0:
                        Route_1.capture()
                        Route_1.ExtractImage()
                        count_r1 = Route_1.vehicles_folder_count_1
                        count_r2 = 0
                        count_r3 = 0
                        Route_4.capture()
                        Route_4.ExtractImage()
                        count_r4 = Route_4.vehicles_folder_count_4
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        
        elif count_r2 == 0 and count_r4 == 0 and count_r1!=0 and count_r3!=0:
                        Route_1.capture()
                        Route_1.ExtractImage()
                        count_r1 = Route_1.vehicles_folder_count_1
                        count_r2 = 0
                        Route_3.capture()
                        Route_3.ExtractImage()
                        count_r3 = Route_3.vehicles_folder_count_3
                        count_r4 = 0
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        
        elif count_r3 == 0 and count_r4 == 0 and count_r1!=0 and count_r2!=0:
                        Route_1.capture()
                        Route_1.ExtractImage()
                        count_r1 = Route_1.vehicles_folder_count_1
                        Route_2.capture()
                        Route_2.ExtractImage()
                        count_r2 = Route_2.vehicles_folder_count_2
                        count_r3 = 0
                        count_r4 = 0
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        
        elif count_r1 != 0 and count_r2 == 0 and count_r3 == 0 and count_r4==0:
                        Route_1.capture()
                        Route_1.ExtractImage()
                        count_r1 = Route_1.vehicles_folder_count_1
                        count_r2 = 0
                        count_r3 = 0
                        count_r4 = 0

                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r1 == 0 and count_r2 != 0 and count_r3 == 0 and count_r4==0:
                        count_r1 = 0
                        Route_2.capture()
                        Route_2.ExtractImage()
                        count_r2 = Route_2.vehicles_folder_count_2
                        count_r3 = 0
                        count_r4 = 0
                        
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r1 == 0 and count_r2 == 0 and count_r3 != 0 and count_r4==0:
                        count_r1 = 0
                        count_r2 = 0
                        Route_3.capture()
                        Route_3.ExtractImage()
                        count_r3 = Route_3.vehicles_folder_count_3
                        count_r4 = 0
                        return setRoute(count_r1, count_r2, count_r3, count_r4)
        elif count_r1 == 0 and count_r2 == 0 and count_r3 == 0 and count_r4!=0:
                        count_r1 = 0
                        count_r2 = 0
                        count_r3 = 0
                        Route_4.capture()
                        Route_4.ExtractImage()
                        count_r4 = setRoute(count_r1, count_r2, count_r3, count_r4)
                        return count_r4
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
                if count_r1 < 15:
                        countdown(5)
                elif count_r1 > 15 and count_r1 < 30:
                        countdown(8)
                else:
                        countdown(10)
                count_r1 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)

        elif count_r2>count_r1 and count_r2>count_r3 and count_r2 > count_r4:
                print("Release Route 2")
                engine_talk("Release Route 2")
                if count_r2 < 15:
                        countdown(5)
                elif count_r2 > 15 and count_r1 < 30:
                        countdown(8)
                else:
                        countdown(10)
                count_r2 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)

        elif count_r3>count_r1 and count_r3>count_r2 and count_r3 > count_r4:
                print("Release Route 3")
                engine_talk("Release Route 3")
                if count_r3 < 15:
                        countdown(5)
                elif count_r3 > 15 and count_r1 < 30:
                        countdown(8)
                else:
                        countdown(10)
                count_r3 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)

        elif count_r4>count_r1 and count_r4>count_r2 and count_r4 > count_r3:
                print("Release Route 4")
                engine_talk("Release Route 4")
                if count_r4 < 15:
                        countdown(5)
                elif count_r4 > 15 and count_r1 < 30:
                        countdown(8)
                else:
                        countdown(10)
                count_r4 = 0
                set_rotation(count_r1, count_r2, count_r3, count_r4)
# count_r1 = int(input("R1:"))
# count_r2 = int(input("R2:"))
# count_r3 = int(input("R3:"))
# count_r4 = int(input("R4:"))
count_r1 = Route_1.vehicles_folder_count_1
count_r2 = Route_2.vehicles_folder_count_2
count_r3 = Route_3.vehicles_folder_count_3
count_r4 = Route_4.vehicles_folder_count_4
setRoute(count_r1, count_r2, count_r3, count_r4)
