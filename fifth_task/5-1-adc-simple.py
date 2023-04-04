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
    for i in range(256):
        dac_signal = bin2dec(i)
        GPIO.output(dac, dac_signal)
        compv = GPIO.input(comp)
        sleep(0.05)

        if compv == 0:
            return i

try:
    while True:
        val = adc()
        if val != 0:
            print(val, '{0:.2f}'.format(3.3 * val / 256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()