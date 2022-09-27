from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time

import motor_module as motor
from motor_module import forward, reverse, stop


#configuration
res = (400,400)
frame_rate = 15
rot = 0


stop_sign = cv.CascadeClassifier('/home/pi/Desktop/Cascade_files/stop_cascade.xml')

#initialize the camera
camera = PiCamera()
camera.resolution = res
camera.rotation = rot
camera.framerate = frame_rate
camera.hflip = True
rawCapture = PiRGBArray(camera, size=res)

#allow the camera to do a push up
time.sleep(0.1)

def pixel_measurement(width, height):
    motor.forward() #default start for the motor
    if(width>=220 and height >= 220):
        # print(width, height)
        #if condition is satisfied, 
        time.sleep(2) # motor continues in its default start state for 2 secs
        motor.stop() # then stops
        time.sleep(1) # sleeps for a second -> Assuming its reading the sign
        motor.reverse() # executes the action it has seen from the sign
        time.sleep(7) # execution happens for the number of seconds 
        motor.stop() # then it stops
#         pass
        

  
def main_camera():
    
    #capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format='bgr',
    use_video_port=True):
        image = frame.array
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        stop_sign_scaled = stop_sign.detectMultiScale(image_gray, 1.05, 7)

        left_sign_scaled = left_sign.detectMultiScale(image_gray, 1.05, 7)
        
        for (x,y,w,h) in stop_sign_scaled:
            #draw a rectangle around the stop sign
            stop_sign_rect = cv.rectangle(image, (x,y),(x+w,y+h),(0,255,0),1)
            width = w
            height = h
#             print(width, height)
            
            pixel_measurement(width, height)
                    
              

        cv.imshow("frame", image)
        key = cv.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord('q'):
            break
            
    
if __name__ == '__main__':    
    main_camera()