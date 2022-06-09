from asyncore import write
import string
import serial
import sys
MAX_BUFF_LEN = 255
counter = 0
port = serial.Serial("COM12",230400,timeout=1)

def read_ser(num_char =1):
    string = port.read(num_char)
    return string.decode()
def write_ser(cmd):
    port.write(cmd.encode())
while True:
    string = read_ser(MAX_BUFF_LEN)
    if(len(string)):
        print(string)
    data = "("+str(counter)+")"
    if(data):
        counter+=1
        write_ser(data)