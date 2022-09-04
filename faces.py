import cv2 as cv
import numpy as np

img = cv.imread('/home/machio_b/Documents/Python/OpenCV_4/Camera/ref_img.jpg')
#resized = cv.resize(img, interpolation=cv.INTER_AREA)

face_classifier = cv.CascadeClassifier('/home/machio_b/Documents/Python/OpenCV_4/cascades/haarcascade_frontalface_default.xml')

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
faces = face_classifier.detectMultiScale(gray, 1.0485258,6)

if faces == ():
    print("no faces found")

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h), (127,0,255), 2)
    cv.imshow('Face Detection', img)
    cv.waitKey(0)
    
cv.destroyAllWindows()