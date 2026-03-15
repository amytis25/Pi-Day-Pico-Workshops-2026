"""
LDR (Light-Dependent Resistor) Sensor Class
Provides a class interface for reading analog light levels from
a photoresistor via ADC, converting raw values to brightness percentages.
"""

import machine

MAX_BRIGHTNESS = 65535 # 16-bit ADC max value
# Class for handling LDR sensor (Photoresistor)
class LDR:
    # Initialize the LDR sensor
    def __init__(self, pin):
        self.ldr = machine.ADC(pin)

    # Read the analog value from the LDR
    def read(self):
        return self.ldr.read_u16()

    # Get the brightness level (0.0 to 1.0)
    def get_brightness(self):
        return (self.read() / MAX_BRIGHTNESS)