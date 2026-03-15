"""
LED Control Class
Provides a class interface for controlling LEDs with methods for
turning on/off, toggling, and PWM brightness control.
"""

import machine
# Class for handling LED pins
class LED:
    # Initialize the LED pin
    def __init__(self, pin_num):
        self.pin = machine.Pin(pin_num, machine.Pin.OUT)

    # Turn the LED on
    def on(self):
        self.pin.value(1)

    # Turn the LED off
    def off(self):
        self.pin.value(0)

    # Toggle the LED
    def toggle(self):
        self.pin.value(not self.pin.value())

    # Set PWM parameters for the LED
    def setPWM(self,freq_hz, duty):
        duty = max(0, min(1, duty))
        self.pwm = machine.PWM(self.pin)
        self.pwm.freq(freq_hz)
        self.pwm.duty_u16(int(duty * 65535))