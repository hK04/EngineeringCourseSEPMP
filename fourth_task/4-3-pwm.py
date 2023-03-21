import RPi.GPIO as GPIO
import sys
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)

pwm = GPIO.PWM(2, 1000)
pwm.start(0)

def dec2bin(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]

try:
    while(True):
        input_ = int(input())
        pwm.ChangeDutyCycle(input_)
        print("{:.2f}".format(input_ * 3.3 / 100))

except ValueError:
    print('Input number is out of range')

except KeyboardInterrupt:
    print('Exit')

finally:
    GPIO.output(dac, 0)
    GPIO.output(2, 0)
    GPIO.cleanup()