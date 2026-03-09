import time
import machine
import random

# pin assignment
button_pullup_pin = 16
button_pulldown_pin = 0
green_led_pin = 15
red_led_pin = 13
best_time = 0

led = machine.Pin (green_led_pin, machine.Pin.OUT)
button = machine.Pin(button_pullup_pin, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    delay = random.uniform(2, 6)   
    print ("Press the button when the green led turns on")
    print ("the game starts!")
    if  button.value() == 0:
        print ("please stop pressing the button")
    time.sleep(delay)
    led.on()
    start_time = time.ticks_ms()
    while button.value() == 1:
        pass
    end_time = time.ticks_ms()
    reaction = time.ticks_diff(end_time, start_time)
    print(f"Your reaction time is: {reaction:.3f} ms")
    if reaction < best_time or best_time == 0:
        best_time = reaction
        print(f"New best time: {best_time:.3f} ms")
    else:
        print(f"Best time: {best_time:.3f} ms")
    led.off()
    time.sleep(3)