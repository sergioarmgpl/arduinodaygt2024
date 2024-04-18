import dht
from machine import Pin,UART
import time

uart = UART(1, 9600)
d = dht.DHT11(machine.Pin(7))

while True:
    print(d.measure())
    t=d.temperature()
    h=d.humidity()
    time.sleep(1)
    uart.write('{"t":'+str(t)+',"h":'+str(h)+'}')   # write the 3 characters
    time.sleep(1)