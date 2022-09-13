from gpiozero import Motor, PWMOutputDevice
import time
import RPi.GPIO as gpio

pwm_pin = 10

#motor pins
m_f_l = [11,9]
m_f_r = [0,5]
m_r_r = [6,13]
m_r_l = [19,26]

motors = [
    Motor(m_f_l[1], m_f_l[0], pwm=False),
    Motor(m_f_r[0], m_f_r[1], pwm=False),
    Motor(m_r_l[0], m_r_l[1], pwm=False),
    Motor(m_r_r[0], m_r_r[1], pwm=False)
]

pwm_out = PWMOutputDevice(pwm_pin)

def forward():   
    motors[0].forward()
    motors[1].forward()
    motors[2].forward()
    motors[3].forward()
    
def reverse():
    motors[0].backward()
    motors[1].backward()
    motors[2].backward()
    motors[3].backward()
    
def right():
    motors[0].forward()
    motors[1].backward()
    motors[2].backward()
    motors[3].forward()
    
def left():
    motors[0].backward()
    motors[1].forward()
    motors[2].forward()
    motors[3].backward()
    
def stop():
    
    motors[0].stop()
    motors[1].stop()
    motors[2].stop()
    motors[3].stop()
    
def destroy():
    stop()
    RPi.GPIO.cleanup()
    
speed = 100
pwm_out.value = (speed/100)

#forward()
#reverse()