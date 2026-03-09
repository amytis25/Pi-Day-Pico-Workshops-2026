from machine import Pin
from machine import ADC
from machine import PWM
import machine
import time
MAX_BRIGHTNESS = 65535
LDR_ADC_Pin = 1
green_led_pin = 15
green_led = PWM(Pin(green_led_pin, Pin.OUT), freq=1000, duty_u16=0)
LDR = ADC(LDR_ADC_Pin)


while True: 
    LDR_val = LDR.read_u16()
    duty_cycle = int((MAX_BRIGHTNESS - LDR_val)*0.9)
    green_led.duty_u16(duty_cycle)
    print(f"brightness: {(LDR_val/MAX_BRIGHTNESS)*100}%")
    print(f"LED Brightness: {(duty_cycle/MAX_BRIGHTNESS)*100}%")
    time.sleep(1)