import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) #broadcom gpio#
GPIO.setwarnings(False)

#class Motor():

def __init__(self, EN=10, IN1A=0, IN2A=5, IN3A=11, IN4A=9, IN1B=6, IN2B=13, IN3B=26, IN4B=19 ):
                       #A -> Front Motor, B-> Back Motors
    #front
    self.EN = EN

    self.IN1A = IN1A
    self.IN2A = IN2A
    self.IN3A = IN3A
    self.IN4A = IN4A

#back
   
    self.IN1B = IN1B
    self.IN2B = IN2B
    self.IN3B = IN3B
    self.IN4B = IN4B
  
#Declare the Pin Modes -> All of them are outputs
    GPIO.setup(self.EN,GPIO.OUT)

    GPIO.setup(self.IN1A,GPIO.OUT)
    GPIO.setup(self.IN2A,GPIO.OUT)
    GPIO.setup(self.IN3A,GPIO.OUT)
    GPIO.setup(self.IN4A,GPIO.OUT)
   
    GPIO.setup(self.IN1B,GPIO.OUT)
    GPIO.setup(self.IN2B ,GPIO.OUT)
    GPIO.setup(self.IN3B ,GPIO.OUT)
    GPIO.setup(self.IN4B ,GPIO.OUT)

    self.PWM1A = GPIO.PWM(self.EN, 60)
    self.PWM1A.start(0.0)

def Forward(self, speed=0, t =0):
    self.PWM1A.ChangeDutyCycle(abs(speed))
    GPIO.output(self.IN1A, GPIO.LOW) #front RIGHT
    GPIO.output(self.IN2A, GPIO.HIGH)

    #self.PWM2A.ChangeDutyCycle(abs(speed))
    GPIO.output(self.IN3A, GPIO.HIGH) #front LEFT
    GPIO.output(self.IN4A, GPIO.LOW)

    #self.PWM1B.ChangeDutyCycle(abs(speed))
    GPIO.output(self.IN1B, GPIO.LOW) #back right
    GPIO.output(self.IN2B, GPIO.HIGH)

    #self.PWM2B.ChangeDutyCycle(abs(speed))
    GPIO.output(self.IN3B, GPIO.LOW) #back left
    GPIO.output(self.IN4B, GPIO.HIGH)

    sleep(t)

def main():
    Forward(40, 5) #spins with a pwm of 60 for 3 seconds

if __name__ == '__main__':
    main()

GPIO.cleanup()