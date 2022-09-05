from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time

from motor_module import stop

#configuration
res = (400,400)
frame_rate = 15
rot = 180


stop_sign = cv.CascadeClassifier('/home/pi/Desktop/Phase_2/Cascade_files/stop_cascade.xml')
right_sign = cv.CascadeClassifier('/home/pi/Desktop/Phase_2/Cascade_files/right_cascade1.xml')
left_sign = cv.CascadeClassifier('/home/pi/Desktop/Phase_2/Cascade_files/left_cascade1.xml')
#initialize the camera
camera = PiCamera()
camera.resolution = res
camera.rotation = rot
camera.framerate = frame_rate
rawCapture = PiRGBArray(camera, size=res)

#allow the camera to do a push up
time.sleep(0.1)
#count = 0
  
def main_camera():
    
    #capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format='bgr',
    use_video_port=True):
        image = frame.array
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        stop_sign_scaled = stop_sign.detectMultiScale(image_gray, 1.3, 5)
        
        for (x,y,w,h) in stop_sign_scaled:
            #draw a rectangle around the stop sign
            stop_sign_rect = cv.rectangle(image, (x,y),(x+w,y+h),(0,255,0),1)
                      
              
        #print(image.shape)
        cv.imshow("frame", image)
        key = cv.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord('q'):
            break
            
    
if __name__ == '__main__':    
    main_camera()