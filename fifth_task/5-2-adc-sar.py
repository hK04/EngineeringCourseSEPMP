import RPi.GPIO as GPIO
import sys 
from time import sleep

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

def bin2dec(n):
    return [int(elem) for elem in bin(n)[2:].zfill(8)]

def adc():
    K = 0
    for i in range(7, -1, -1):
        K += 2 ** i
        GPIO.output(dac,  bin2dec(K))
        sleep(0.05)
        if GPIO.input(comp) == 0:    
            K -= 2 ** i
    return K


try:
    while True:
        val = adc()
        if val != 0:
            print(val, '{0:.2f}'.format(3.3 * val / 256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()