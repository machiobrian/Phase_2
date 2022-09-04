from gpiozero import Motor, PWMOutputDevice
from time import sleep
pwm_pin = 10 # single pwm pinsubject to change

# initialize the motor pins
f_left = [9,11]
f_right = [5,0]
b_left = [13,6]
b_right = [26,19]

motors = [
    Motor(b_left[1], b_left[0], pwm=False),
    Motor(b_right[0],b_right[1], pwm=False),
    Motor(f_left[1], f_left[0], pwm=False), 
    Motor(f_right[0],f_right[1], pwm=False)
] #removes the need for manual re-wiring at the l298 driver
  #can change the IN(X) pins from the code
pwm_out = PWMOutputDevice(pwm_pin)
speed = 75
pwm_out.value = (speed/100) #convert from % to float 0 to 1

def move_forward():
    motors[0].forward()
    motors[1].forward()
    motors[2].forward()
    motors[3].forward()

def move_reverse():
    motors[0].backward()
    motors[1].backward()
    motors[2].backward()
    motors[3].backward()

def move_right():
    motors[0].forward()
    motors[1].backward()
    motors[2].backward()
    motors[3].forward()

def move_left():
    motors[0].backward()
    motors[1].forward()
    motors[2].forward()
    motors[3].backward()

def stop():
    motors[0].stop()
    motors[1].stop()
    motors[2].stop()
    motors[3].stop()