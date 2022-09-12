import RPi.GPIO as GPIO
import time

#ccw or cw rotation is only enabled by a single pin,
# for front left, set 9->True and 11-> False to have one of the two
# motions

def clear_pins():
    GPIO.cleanup()

def init():
    GPIO.setmode(GPIO.BCM) #using the broad com soc referncing

    GPIO.setup(9,GPIO.OUT) #front left
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(5,GPIO.OUT) #front right
    GPIO.setup(0,GPIO.OUT)

    GPIO.setup(13,GPIO.OUT) #rear left
    GPIO.setup(6,GPIO.OUT)
    GPIO.setup(26,GPIO.OUT) #rear right
    GPIO.setup(19,GPIO.OUT)

    GPIO.setup(10, GPIO.OUT)

def forward(seconds): # all motor run, set all to True
    init()
    GPIO.output(10, True)
    GPIO.output(9, True) #cw
    GPIO.output(11, False)

    GPIO.output(5, True)
    GPIO.output(0, False)

    GPIO.output(13, True)
    GPIO.output(6, False)

    GPIO.output(26, True)
    GPIO.output(19, False)
    clear_pins()

def reverse(seconds):
    init()
    GPIO.output(9, False) #ccw
    GPIO.output(11, True)

    GPIO.output(5, False)
    GPIO.output(0, True)

    GPIO.output(13, False)
    GPIO.output(6, True)

    GPIO.output(26, False)
    GPIO.output(19, True)
    clear_pins()

def right(seconds):
    init()
    GPIO.output(9, True) #cw
    GPIO.output(11, False)

    GPIO.output(5, False)
    GPIO.output(0, True)

    GPIO.output(13, False)
    GPIO.output(6, True)

    GPIO.output(26, True)
    GPIO.output(19, False)
    clear_pins()

def left(seconds):
    init()
    GPIO.output(9, False) #ccw
    GPIO.output(11, True)

    GPIO.output(5, True)
    GPIO.output(0, False)

    GPIO.output(13, True)
    GPIO.output(6, False)

    GPIO.output(26, False)
    GPIO.output(19, True)
    clear_pins()

def rot_p90(seconds):
    init()
    GPIO.output(9, True) #cw
    GPIO.output(11, False)

    GPIO.output(5, False)
    GPIO.output(0, True)

    GPIO.output(13, True)
    GPIO.output(6, False)

    GPIO.output(26, False)
    GPIO.output(19, True)
    clear_pins()

def rot_n90(seconds):
    GPIO.output(9, False) #ccw
    GPIO.output(11, True)

    GPIO.output(5, True)
    GPIO.output(0, False)

    GPIO.output(13, False)
    GPIO.output(6, True)

    GPIO.output(26, True)
    GPIO.output(19, False)
    clear_pins()