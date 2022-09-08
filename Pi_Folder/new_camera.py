from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time

import motor_module as motor
from motor_module import forward, reverse, stop

import argparse #used f command line arguments
import os

#configuration
res = (400,400)
frame_rate = 15
rot = 0

#construct the argument parser and parse te arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c","--Cascade_files", type=str, default="Cascade_files",
                help="path containing haar cascades")
args = vars(ap.parse_args())                

detector_paths = {
    "stop" : "stop_cascade.xml",
    "right" : "right_cascade1.xml",
    "left" : "left_cascade1.xml"
    
}

detectors = {}

for (name, path) in detector_paths.items():
    path = os.path.sep.join([args["Cascade_files"], path])
    detectors[name] = cv.CascadeClassifier(path)

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
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        img_scaled = detectors["stop"].detectMultiScale(gray, 1.3, 2)
        img1_scaled = detectors["right"].detectMultiScale(gray, 1.3, 2)

        for (x,y,w,h) in img1_scaled:
                face_rect = cv.rectangle(image, (x,y),(x+w,y+h),(0,23,256),2)
                width = w
                height = h
                pixel_measurement(width, height)
        for (x,y,w,h) in img_scaled:
                eyes_rect = cv.rectangle(image, (x,y),(x+w,y+h),(0,23,256),2)
                width = w
                height = h          
                pixel_measurement(width, height)

        cv.imshow("frame", image)
        key = cv.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord('q'):
            break                                    
            
    
if __name__ == '__main__':    
    main_camera()