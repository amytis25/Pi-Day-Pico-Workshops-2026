"""
Blink LED Tutorial
Toggles an LED on and off using GPIO pin 15.
Basic example demonstrating digital output on Raspberry Pi Pico.
"""

import machine
import time

led = machine.Pin(15, machine.Pin.OUT)

# on board led
# led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
    # can change value manually using:
    # led.value(1)  # turn on
    # led.value(0)  # turn off