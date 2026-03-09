import machine
import time

green_led = machine.Pin(15, machine.Pin.OUT)
red_led = machine.Pin(13, machine.Pin.OUT)
button_pulldown = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pullup = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    if not button_pulldown.value():
        green_led.value(0)
    else:
        green_led.value(1)

    if not button_pullup.value():
        red_led.value(1)
    else:
        red_led.value(0)

""" Interrupt example

button_pulldown = Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pullup = Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

def green_button_handler(pin):
    green_led.toggle()

def red_button_handler(pin):
    red_led.toggle()

button_pulldown.irq(trigger=machine.Pin.IRQ_RISING, handler=green_button_handler)
button_pullup.irq(trigger=machine.Pin.IRQ_FALLING, handler=red_button_handler)
"""