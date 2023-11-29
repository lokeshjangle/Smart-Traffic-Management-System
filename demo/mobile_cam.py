import requests
import imutils
import cv2
import numpy as np
import time
import glob

url = "http://192.168.58.105:8080/shot.jpg"

# while True:
#     img_resp = requests.get(url)
#     img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
#     img = cv2.imdecode(img_arr,-1)
#     img = imutils.resize(img,width=1000,height=1000)
#     cv2.imshow("Android_cam",img)
#     if cv2.waitKey(1) == 27:
#         break
# cv2.destroyAllWindows()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Video/Video_r1.avi',fourcc,20.0,(640,480))
cap_duration = 5
cap = cv2.VideoCapture(1)
start_time = time.time()
while (int(time.time()-start_time) < cap_duration):
    ret,frame = cap.read()
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    img = imutils.resize(img,width=1000,height=1000)
    if ret == True:
        out.write(frame)
        cv2.imshow('Video',frame)
        cv2.waitKey(5) 
    else:
        break   
cap.release()
out.release()
cv2.destroyAllWindows()
