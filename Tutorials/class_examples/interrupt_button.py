import machine

class Button_pullup:

    def __init__(self, pin_num, trigger, callback):
        self.pin = machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_UP)
        self.callback = callback

        self.pin.irq(
            trigger=trigger,
            handler=self._irq_handler
        )

    def _irq_handler(self, pin):
        self.callback()

class Button_pulldown:

    def __init__(self, pin_num, trigger, callback):
        self.pin = machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.callback = callback

        self.pin.irq(
            trigger=trigger,
            handler=self._irq_handler
        )

    def _irq_handler(self, pin):
        self.callback()