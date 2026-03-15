"""
Light-Dependent Resistor (LDR) Example
Reads analog values from an LDR sensor and controls LED brightness
using PWM based on ambient light levels. Demonstrates ADC and PWM usage.
"""

from machine import Pin
from machine import ADC
from machine import PWM
import machine
import time
MAX_BRIGHTNESS = 65535 # 16-bit ADC max value
LDR_ADC_Pin = 1
green_led_pin = 15
green_led = PWM(Pin(green_led_pin, Pin.OUT), freq=1000, duty_u16=0) # set PWM parameters
LDR = ADC(LDR_ADC_Pin) # set ADC pin


while True: 
    LDR_val = LDR.read_u16() # read the analog value from the LDR
    duty_cycle = int((MAX_BRIGHTNESS - LDR_val)*0.9) # calculate new brightness 
    green_led.duty_u16(duty_cycle) # set duty cycle
    print(f"brightness: {(LDR_val/MAX_BRIGHTNESS)*100}%")
    print(f"LED Brightness: {(duty_cycle/MAX_BRIGHTNESS)*100}%")
    time.sleep(1)