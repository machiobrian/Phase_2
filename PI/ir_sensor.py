from gpiozero import LineSensor
import RPi.GPIO as GPIO
import ip_rasp
ip_rasp = ip_rasp()


try:
    sensor = LineSensor(4) #GPIO4
    

    while True:
        if sensor.value<0.5: #black line/surface
            #call the camera module
            ip_rasp()

            print('Line detected')
        else: #white surface
            break

except:
    GPIO.cleanup()