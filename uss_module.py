#function distance to return current distance infront of the USS
#stops the car when some obstacles are in infron of the car

#------------import libs and initialize pins
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIG = 4 #pin number 4
GPIO_ECHO = 17

GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIG, False)

class USS():
    def Distance(self):
        #trigger the USS for a short time
        GPIO.output(GPIO_TRIG, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIG, False)

        while GPIO.input(GPIO_ECHO) == 0:
            pass
        StartTime = time.time() #restart the timer
        while GPIO.input(GPIO_ECHO) == 1:
            pass
        StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        speed = 34300 #speed of sound in air 343m/s
        distance = (TimeElapsed*speed)/2
        time.sleep(0.01)
        return round(distance, 2)