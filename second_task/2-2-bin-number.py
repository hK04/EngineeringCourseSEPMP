import RPi.GPIO as GPIO 
import time
import random
#from matplotlib.pyplot import plt

bytes_ = [1, 0]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
#number = [0] * 8
#
#for i in number:
#    number[i] = random.choice(bytes_)
number_two = [1] * 8 

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number_two)

time.sleep(15)

GPIO.output(dac, 0)


GPIO.cleanup()