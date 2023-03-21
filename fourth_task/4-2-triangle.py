import RPi.GPIO as GPIO
import sys
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]

try:
    while(True):
        input_ = input()

        if not input_.isdigit():
            print('Input is not a number')
        
        t_ = int(input_) / 256 / 2

        for i in range(256):
            GPIO.output(dac, dec2bin(i, 8))
            sleep(t_)

        for i in range(255, -1, -1):
            GPIO.output(dac, dec2bin(i, 8))
            sleep(t_)

except ValueError:
    print('Input number is out of range')

except KeyboardInterrupt:
    print('Exit')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()