import cv2
import os
# from Capture import captureImage

# captureImage.capture()
class Extract():
    def capture():
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('Video/cap_video.avi',fourcc,20.0,(640,480))

            cap = cv2.VideoCapture(0)
            while True:
                ret,frame = cap.read()

                out.write(frame)
                cv2.imshow('Video',frame)
                cv2.waitKey(5) 
                break

            cap.release()
            out.release()
            cv2.destroyAllWindows()
    def ExtractImage():
        # cam = cv2.VideoCapture("Video/cap_video.avi")
        cam = cv2.VideoCapture("video.mp4")

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
                name = './Image/frame' + '.jpg'
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


    # capture()
    ExtractImage()
# Read the video from specified path
