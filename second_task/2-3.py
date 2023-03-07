import RPi.GPIO as GPIO 
import time



aux  = [2,3,14,15,18,27,23,22]
leds = [24,25,8,7,12,16,20,21]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

GPIO.output(leds,0)
time.sleep(2)
while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))