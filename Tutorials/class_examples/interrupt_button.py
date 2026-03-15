"""
Interrupt Button Classes
Provides Button_pullup and Button_pulldown classes for handling
button input using hardware interrupts instead of polling.
"""

import machine
# Class for handling pull-up buttons as interrupts
class Button_pullup:
    # Initialize the pull-up button
    def __init__(self, pin_num, trigger, callback):
        self.pin = machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_UP)
        self.callback = callback

        self.pin.irq(
            trigger=trigger,
            handler=self._irq_handler
        )
    # Interrupt handler
    def _irq_handler(self, pin):
        self.callback()


# Class for handling pull-down buttons as interrupts
class Button_pulldown:
    # Initialize the pull-down button
    def __init__(self, pin_num, trigger, callback):
        self.pin = machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.callback = callback

        self.pin.irq(
            trigger=trigger,
            handler=self._irq_handler
        )
    # Interrupt handler
    def _irq_handler(self, pin):
        self.callback()