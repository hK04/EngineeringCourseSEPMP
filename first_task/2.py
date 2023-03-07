import RPi.GPIO as GIO
from time import sleep

GIO.setmode(GIO.BCM)

sleep(0.5)

GIO.setup(22, GIO.IN)
GIO.setup(27, GIO.OUT)

if GIO.input(22):
    GIO.output(27, 1)
else:
    GIO.output(27, 0)