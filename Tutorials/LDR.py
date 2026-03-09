import machine

MAX_BRIGHTNESS = 65535

class LDR:
    def __init__(self, pin):
        self.ldr = machine.ADC(pin)

    def read(self):
        return self.ldr.read_u16()

    def get_brightness(self):
        return (self.read() / MAX_BRIGHTNESS)