import os
import cv2
import time
import glob
from vehicle_detector import VehicleDetector
# from ExtractImage import Extract

# from Capture import captureImage

# captureImage.capture()
class Route_1():
    def capture():
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter('Video/Video_r1.avi',fourcc,20.0,(640,480))
                cap_duration = 5
                cap = cv2.VideoCapture(0)
                start_time = time.time()
                while (int(time.time()-start_time) < cap_duration):
                    ret,frame = cap.read()

                    if ret == True:
                        out.write(frame)
                        cv2.imshow('Video',frame)
                        cv2.waitKey(5) 
                    else:
                        break   

                cap.release()
                out.release()
                cv2.destroyAllWindows()

    def ExtractImage():
            cam = cv2.VideoCapture("Video/cap_video.avi")
            #cam = cv2.VideoCapture("video.mp4")

            try:
                
                # creating a folder named data
                if not os.path.exists('Image'):
                    os.makedirs('Image')
            
            # if not created then raise error
            except OSError:
                print ('Error: Creating directory of data')
            
            # frame
            currentframe = 0
            
            # while(True):
                
                # reading from frame
            ret,frame = cam.read()
            
            if ret:
                    # if video is still left continue creating images
                    name = './Image/frame_r1' + '.jpg'
                    print ('Creating...' + name)
            
                    # writing the extracted images
                    cv2.imwrite(name, frame)
            
                    # increasing counter so that it will
                    # show how many frames are created
                    currentframe = 1
            else:
                currentframe = 0
            
            # Release all space and windows once done
            cam.release()
            cv2.destroyAllWindows()


    capture()
    ExtractImage()
    # Read the video from specified path

    # ex = Extract()

    # Load Veichle Detector
    vd = VehicleDetector()

    # Load images from a folder
    images_folder = glob.glob("Image/frame_r1.jpg")

    vehicles_folder_count_1 = 0

    # Loop through all the images
    for img_path in images_folder:
        print("Img path", img_path)
        img = cv2.imread(img_path)

        vehicle_boxes = vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)

        # Update total count
        vehicles_folder_count_1 += vehicle_count

        for box in vehicle_boxes:
            x, y, w, h = box

            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

        cv2.imshow("Cars", img)
        cv2.waitKey(500)

    os.remove("Image/frame_r1.jpg")
    os.remove("Video/Video_r1.avi")
    print("Total current count", vehicles_folder_count_1)
    time.sleep(5)