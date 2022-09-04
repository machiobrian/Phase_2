from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time

#configuration
res = (320,240)
frame_rate = 15

stop_sign = cv.CascadeClassifier('/home/pi/Phase_/Phase_1/cascade_stop_sign.xml')

#initialize the camera
camera = PiCamera()
camera.resolution = res
camera.framerate = frame_rate
rawCapture = PiRGBArray(camera, size=res)

#allow the camera to do a push up
time.sleep(0.1)
count = 0

def camera_stream():
    #capture frames from stream
    for frame in camera.capture_continuous(rawCapture, format='bgr',
use_video_port=True):
        image = frame.array
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        stop_sign_scaled = stop_sign.detectMultiScale(image_gray, 1.3, 2)
        
        #detect sign and draw rectangle round it
        for (x,y,w,h) in stop_sign_scaled:
            global stop_w
            stop_w = w
            global stop_h
            stop_h = h
            #print(stop_w, stop_h)
            measure_pixel()

            
#distance function
def measure_pixel():
    """Since we have w and h, use it to determine dist from sign
    distance = far, close, stop"""
    #print(stop_w) #ccall this function inside a function
    pixel = 200
    max_pixel = 600
    if stop_w in range(pixel, max_pixel) and stop_h in range(pixel, max_pixel):
        print("stop bot")
    else:
        print("safe")