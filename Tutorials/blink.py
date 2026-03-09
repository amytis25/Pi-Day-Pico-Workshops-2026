import machine
import time

led = machine.Pin(15, machine.Pin.OUT)

# on board led
# led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)