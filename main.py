from machine import Pin, ADC
from servo import Servo
import time

def sleep(seconds):
    time.sleep_ms(int(seconds*1000))


s = Servo(Pin(13), max_us=2500)
adc = ADC(Pin(12))

def eat():
    sleep(.5)
    
    s.write_angle(90)
    sleep(.5)
    s.write_angle(10)
    sleep(.3)
    s.write_angle(70)
    sleep(.5)

    # after ate
    for _ in range(3):
        s.write_angle(50)
        sleep(.25)
        s.write_angle(70)
        sleep(.25)

    s.write_angle(90)
    sleep(.1)
    
print("Eating time")
s.write_angle(90)
prev_value = 0
while True:
    value = adc.read()
    print("Value: ", value)
    # from outsize to inside
    if prev_value <= 4000:
        if value > 4000:
            # prevent shake
            sleep(.2)
            value = adc.read()
            if value > 4000:
                print('action:', value)
                eat()
    prev_value = value
    sleep(.2)
