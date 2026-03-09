import machine

class LED:
    def __init__(self, pin_num):
        self.pin = machine.Pin(pin_num, machine.Pin.OUT)

    def on(self):
        self.pin.value(1)

    def off(self):
        self.pin.value(0)

    def toggle(self):
        self.pin.value(not self.pin.value())

    def setPWM(self,freq_hz, duty):
        self.pwm = machine.PWM(self.pin)
        self.pwm.freq(freq_hz)
        self.pwm.duty_u16(int(duty * 65535))