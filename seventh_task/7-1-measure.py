import RPi.GPIO as gpio
import time
from matplotlib import pyplot

gpio.setmode(gpio.BCM)

leds=[21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)

dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)

comp=4
troyka=17 
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, dec2bin(k))
        time.sleep(0.005)
        if gpio.input(comp)==0:
            k-=2**i
    return k

def dec2bin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

try:
    napr=0
    result_ismer=[]
    time_start=time.time()
    count=0

    #charge of capacitor
    print('Charge of capacitor')
    while napr<256*0.25:
        napr=adc()
        result_ismer.append(napr)
        time.sleep(0)
        count+=1
        gpio.output(leds, dec2bin(napr))

    gpio.setup(troyka,gpio.OUT, initial=gpio.LOW)

    #decharge of capacitor
    print('Decharge of Capacitor')
    while napr>256*0.02:
        napr=adc()
        result_ismer.append(napr)
        time.sleep(0)
        count+=1
        gpio.output(leds, dec2bin(napr))

    time_experiment=time.time()-time_start

    print('Writing data into file')
    with open('data.txt', 'w') as f:
        for i in result_ismer:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01289')
    
    print('Full experiment time {}, Period of one measurement {}, medium frequency of discretisation {}, step of ADC {}'.format(time_experiment, time_experiment/count, 1/time_experiment/count, 0.013))

    #graphics
    print('Plot')
    y=[i / 256 * 3.3 for i in result_ismer]
    x=[i * time_experiment/count for i in range(len(result_ismer))]
    pyplot.plot(x, y)
    pyplot.xlabel('t, s')
    pyplot.ylabel('V, Vlt')
    pyplot.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()