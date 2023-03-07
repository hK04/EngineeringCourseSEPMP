import RPi.GPIO as GPIO 
import time
import random
#from matplotlib.pyplot import plt

GPIO.cleanup()
bytes_ = [1, 0]

aux  = [22, 23, 27, 18, 15, 14, 3, 2]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
#number = [0] * 8
#
#for i in number:
#    number[i] = random.choice(bytes_)
number_two = [1] * 8 

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while KeyboardInterrupt():
    for i in range(len(leds)):
        GPIO.output(leds[i], GPIO.input(aux[i]))

