import pycom
pycom.heartbeat(False)

def led_red( ):
    pycom.rgbled(0xFF0000)
def led_lightred( ):
    pycom.rgbled(0xFF2000)
def led_violet( ):
    pycom.rgbled(0xFF00FF)
def led_blue( ):
    pycom.rgbled(0x0000FF)
def led_green( ):
    pycom.rgbled(0x00FF00)

from network import LoRa
import socket
import binascii
import struct
from time import sleep

led_red()

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868) #,tx_iq=True,adr=True)#

app_eui = binascii.unhexlify('70B3D57ED0010D30')
app_key = binascii.unhexlify('7C70118B619BB0D55C76CDC4B3F7E0C2')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    led_lightred()
    sleep(0.2)
    led_red()
    sleep(0.2)

led_blue()
sleep(1)

led_violet()
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(True)
s.send(bytes([1, 2, 3]))

led_green()
sleep(2)
