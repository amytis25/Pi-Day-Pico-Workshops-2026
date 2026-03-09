import time
import machine
from interrupt_button import Button_pulldown
from interrupt_button import Button_pullup
from LDR import LDR
from LED import LED

## pin assignments
button_pullup_pin = 16
button_pulldown_pin = 0
green_led_pin = 15
red_led_pin = 13
ldr_pin = 1

## defaults
red_led_duty = 0.5
green_led_duty = 0.5
red_led_freq = 1000
green_led_freq = 1000

red_led = LED(red_led_pin)
green_led = LED(green_led_pin)
ldr = LDR(ldr_pin)


def setPWM():
    red_led.setPWM(red_led_freq, red_led_duty)
    green_led.setPWM(green_led_freq, green_led_duty)

def increasePWM():
    global red_led_duty, green_led_duty
    next_red_led_duty = red_led_duty + 0.1
    next_green_led_duty = green_led_duty + 0.1
    if next_red_led_duty <= 1.0:
        red_led_duty = next_red_led_duty
    else:
        red_led_duty = 0
    if next_green_led_duty <= 1.0:
        green_led_duty = next_green_led_duty
    else: 
        green_led_duty = 0
    setPWM()

def decreasePWM():
    global red_led_duty, green_led_duty
    next_red_led_duty = red_led_duty - 0.1
    next_green_led_duty = green_led_duty - 0.1
    if next_red_led_duty >= 0:
        red_led_duty = next_red_led_duty
    else:
        red_led_duty = 1
    if next_green_led_duty >= 0:
        green_led_duty = next_green_led_duty
    else:
        green_led_duty = 1
    setPWM()

button_pullup = Button_pullup(button_pullup_pin, machine.Pin.IRQ_FALLING, decreasePWM)
button_pulldown = Button_pulldown(button_pulldown_pin, machine.Pin.IRQ_FALLING, increasePWM)

def main():
    setPWM()
    while True:
        ldr_value = ldr.get_brightness()
        print(f"LDR Value: {(ldr_value * 100):.2f}%")
        time.sleep(1)



if __name__ == "__main__":
    main()