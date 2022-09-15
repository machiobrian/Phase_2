from picamera.array import PiRGBArray
import RPi.GPIO as GPIO
from picamera import PiCamera

import time
import cv2 as cv
import numpy as np
import math

GPIO.setmode(GPIO.BOARD) #use the sequence 1-40
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

theta = 0
minlineLength = 5
maxLineGap = 10

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640,480))
time.sleep(0.1) #camera pushup

for frame in camera.capture_continuous(rawCapture, format="bgr",
use_video_port = True):
    image  = frame.array
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5,5), 0)
    edged = cv.HoughLinesP(edged,1,np.pi/180,10,minlineLength, maxLineGap)

    if (lines != None): #if there are lines
        for x in range(0, len(lines)):
            for x1,y1,x2,y2 in lines[x]:
                cv.line(image, (x1,y1), (x2,y2),(0,255,0),2)
                theta = theta+math.atan2((y2-y2),(x2-x1))

    threshold = 6
    if(theta > threshold):
        GPIO.output(7,True)
        GPIO.output(8,False)
        print('left')

    if (theta<-threshold):
        GPIO.output(7,False)
        GPIO.output(8,True)
        print('right')
    if (abs(theta)<threshold):
        GPIO.output(7,False)
        GPIO.output(8,False)
        print('straight')

    theta = 0
    cv.imshow("Frame", image)
    key = cv.waitKey(1) & 0xFF
    rawCapture.truncat(0)

    if key==ord("q"):
        break