import pycom
pycom.heartbeat(False)
pycom.rgbled(0xFF0000)  # Red

from network import LoRa
import socket
import ubinascii
import struct
import time

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN,tx_iq=True,adr=True)#, region=LoRa.EU868)

# create an ABP authentication params


dev_addr = struct.unpack(">l", ubinascii.unhexlify('26011DE5'))[0]
nwk_swkey = ubinascii.unhexlify('EBBB4006A7F59EBE78EB9759FAD64F4E')
app_swkey = ubinascii.unhexlify('05E0BBA98130AB80D3B3DBAE90E0316A')

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey), timeout=20000)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)
#s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data

pycom.rgbled(0xFF00FF)
#print("Lets pray...")
#print(s.send)
s.send(bytes([0x01, 0x02, 0x03]))
#s.send('Hello World')

#s.setblocking(False)
#data = s.recv(64)
#s.close()

pycom.rgbled(0x00FF00)  # Green

#quit()

## make the socket non-blocking
## (because if there's no data received it will block forever...)
#s.setblocking(False)
#
## get any data received (if any...)
#data = s.recv(64)
#print(data)
