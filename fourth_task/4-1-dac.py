import RPi.GPIO as GPIO
import sys

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]

try:
    while(True):
        input_ = input('Input value from 0 to 255: \n')

        if input_ == 'q':
            sys.exit()
        elif input_.isdigit() and int(input_ ) % 1 == 0 and 0 <= int(input_ ) <= 255:
            GPIO.output(dac, dec2bin(int(input_), 8))
            print('{:.4f}'.format(int(input_) / 256 * 3.3))
        elif not input_.isdigit():
            print('Input number is out of range')

except ValueError:
    print('Input number is out of range')

except KeyboardInterrupt:
    print('Exit')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()