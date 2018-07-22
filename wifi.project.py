wifissid = 'wlanfh1x'
wifiuser = 'SRHK.SRH.DE\\***********'
wifipassword = '***********'
#wifissid = 'pycom1'
#wifipassword = 'testtest42'

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

from network import WLAN
from time import sleep
wlan = WLAN(mode=WLAN.STA)

led_red()
sleep(0.5)
nets = wlan.scan()
for net in nets:
    if net.ssid == wifissid:
        led_lightred()
        #wlan.connect(net.ssid, auth=(WLAN.WPA2, wifipassword), timeout=20000)
        wlan.connect(net.ssid, auth=(WLAN.WPA2_ENT, wifiuser, wifipassword), identity=wifiuser, timeout=20000)
        while not wlan.isconnected():
            led_lightred()
            sleep(0.2)
            led_orange()
            sleep(0.2)
        led_blue()
        break

