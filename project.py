import pycom
pycom.heartbeat(False)
def led_red( ):
    pycom.rgbled(0xFF0000)
def led_lightred( ):
    pycom.rgbled(0xFF2000)
def led_orange( ):
    pycom.rgbled(0xFF9000)
def led_violet( ):
    pycom.rgbled(0xFF00FF)
def led_blue( ):
    pycom.rgbled(0x0000FF)
def led_green( ):
    pycom.rgbled(0x00FF00)

import time
import uos
from machine import Pin


pir = Pin('G4',mode=Pin.IN, pull=Pin.PULL_UP)

def rand_i_up_to(n):
    return uos.urandom(1)[0] % (n+1)

for i in range(2+rand_i_up_to(3)):
    led_blue()
    time.sleep_ms(500)
    led_violet()
    time.sleep_ms(500)
led_blue()
time.sleep_ms(50*rand_i_up_to(3))

poll_each_ms = 20
stable_for = 0
last_value = 1
stability_required = 200

while True:
    new_value = pir()
    if new_value != last_value:
        stable_for = 0
    else:
        stable_for += poll_each_ms

    if stable_for >= stability_required:
        stable_for = stability_required
        if new_value == 1:
            led_green()
        else:
            led_red()

    last_value = new_value
    time.sleep_ms(poll_each_ms)

