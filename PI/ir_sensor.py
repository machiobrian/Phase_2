from gpiozero import LineSensor
sensor = LineSensor(4) #GPIO4
while True:
    if sensor.value<0.5: #black line/surface
         print('Line detected')
    else: #white surface
        print('No line detected')
