import RPi.GPIO as GIO
from time import sleep

GIO.setmode(GIO.BCM)

sleep(0.5)

GIO.setup(22, GIO.OUT)

for i in range(10):
    GIO.output(22, 1)
    sleep(0.5)
    GIO.output(22, 0)
    sleep(0.5)