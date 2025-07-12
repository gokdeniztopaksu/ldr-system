from machine import ADC, Pin
from time import sleep_us as yd_us, sleep as yd
import time 

led = Pin(15, Pin.OUT)
buzzer = Pin(2, Pin.OUT)
ldr = ADC(Pin(26))
trig = Pin(3, Pin.OUT)
echo = Pin(6, Pin.IN)

ldr_threshold = 1
distance_thresold = 20

def get_distance():
    trig.low()
    yd_us(2)
    
    trig.high()
    yd_us(10)
    trig.low()
    
    while echo.value() == 0:
        pulse_start = time.ticks_us()
        
    while echo.value() == 1:
        pulse_end = time.ticks_us()
        
    duration = time.ticks_diff(pulse_end, pulse_start)
    distance_cm = (duration / 2) / 29.1
    return distance_cm

def get_light():
    value = ldr.read_u16()
    voltage = value * 3.3 / 65535
    return round(voltage, 2)

def led_on():
    led.value(1)

def led_off():
    led.value(0)
        
def buzz():
    for _ in range(4):
        buzzer.value(1)
        yd(0.2)
        buzzer.value(0)
        yd(0.2)
        
def buzzer_off():
    buzzer.value(0)



while True:
    light = get_light()
    distance = get_distance()
    
    print("Light:", light, "Distance:", distance, round(distance, 1), "cm.")
    
    if light <= ldr_threshold:
        led_on()
        if distance < distance_thresold:
            buzz()
        else:
            buzzer_off()
    else:
        led_off()
        buzzer_off()
        
    yd(0.2)