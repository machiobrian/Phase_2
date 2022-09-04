#initialize camera
import cv2 as cv
def camera_init():
    from picamera import PiCamera 
    global camera
    camera = PiCamera()

def cam_settings():
    import time
    res = (320,240)
    frame_rate = 15
    camera.resolution = res
    camera.framerate = frame_rate
    global rawCapture
    rawCapture = camera.array.PiRGBArray(camera, size=res)
    #camera push-up
    time.sleep(0.1)

def camera_stream():
    #capture frames from screen
    for frame in camera.capture_continuous(rawCapture, format='bgr',
    use_video_port=True):
        image = frame.array
        image_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        