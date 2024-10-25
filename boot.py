# coding: utf-8
#
# ESP32-C3
#
# codeskyblue 2024-10-24

from machine import Pin, ADC
from servo import Servo
import time

def sleep(seconds):
    time.sleep_ms(int(seconds*1000))

led = Pin(8, Pin.OUT) # LED
s = Servo(Pin(4), max_us=2500)
adc = ADC(Pin(3))
adc.atten(3) # 11dB attenuation


def led_on():
    led.value(0)

def led_off():
    led.value(1)


def eat(s: Servo):
    sleep(.2)
    s.write_angle(90)
    sleep(.5)
    s.write_angle(10)
    sleep(.3)
    s.write_angle(70)
    sleep(.5)

    # bite
    for _ in range(3):
        s.write_angle(50)
        sleep(.25)
        s.write_angle(70)
        sleep(.25)

    s.write_angle(90)
    sleep(.1)


THRESHOLD = 3200

def read_adc_value() -> int:
    v1 = adc.read()
    time.sleep_ms(10)
    v2 = adc.read()
    return min(v1, v2)
    

def main():
    print("eating robot is ready")
    s.write_angle(90)
    prev_value = 0
    led_on()

    while True:
        value = read_adc_value()
        print("value:", value)
        if value > THRESHOLD:
            led_on()
        else:
            led_off()
        
        # from inside to output
        if prev_value > THRESHOLD: # inside
            if value <= THRESHOLD: # outsize
                sleep(.2)
                print('action:', value)
                eat(s)
        prev_value = value

if __name__ == '__main__':
    main()
