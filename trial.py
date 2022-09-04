import cv2 as cv
#import motor_module_dummy as mot
from motor_module_dummy import move_forward, stop, move_left

def process_image(sign):
    #self.sign = sign
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    sign_scaled = sign.detectMultiScale(gray, 1.3, 2)

    #detect sign and draw rect around it
    for (x,y,w,h) in sign_scaled:
        sign_rect = cv.rectangle(img, (x,y), (x+w, y+h), (0,255,256),3)
    cv.imshow("image", img)

def move_right():
    print("right")


#load classifiers to objects, hereafter we use objects
stop_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/stop_cascade.xml')
left_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/left_cascade1.xml')
right_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/right_cascade1.xml')

#create a tuple to store the signs
sign_tuple = ('stop_sign', 'right_sign', 'left_sign')

cap = cv.VideoCapture(0)
while cap.isOpened():
    
    _,img = cap.read()

    # if left_sign:
    #     process_image(left_sign)
    #     mot.move_left
    if stop_sign:
        process_image(stop_sign)
        stop
    if right_sign:
        process_image(right_sign)
        move_right()

    # for x in sign_tuple():
    #     if left_sign:
    #         process_image(left_sign)
    #     elif stop_sign:
    #         process_image(stop_sign)
    #     elif right_sign:
    #         process_image(right_sign)







    key=cv.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break



