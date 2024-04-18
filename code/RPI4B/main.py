import time
import redis
import os
import sys
import json

import serial
from time import sleep

rhost = os.environ['REDIS_HOST']
rauth = os.environ['REDIS_AUTH']
r = redis.StrictRedis(host=rhost,\
        port=6379,db=0,password=rauth,\
        decode_responses=True)

device = os.environ['DEVICE']
baudrate = int(os.environ['BAUD_RATE'])
ser = serial.Serial (device,baudrate)  #Open port with baud rate
while True:
    print({"msg":"waiting for read"},file=sys.stderr)
    received_data = ser.read() #read serial port
    sleep(0.03)
    data_left = ser.inWaiting() #check for remaining byte
    received_data+=ser.read(data_left)
    received_data=received_data.decode('utf-8')
    print({"msg":"received"},file=sys.stderr)
    #transform data
    json_data = json.loads(received_data)
    t=json_data["t"]
    h=json_data["h"]
    r.set("temperature",t)
    r.set("humidity",h)
    print({"t":t},file=sys.stderr)
    print({"h":h},file=sys.stderr)
    print({"processed":"done"},file=sys.stderr)