import serial
from mysql_upload import upload as my_upload

# need change
port_name = "/dev/cu.usbmodem1411"
area = str(301)

with serial.Serial(port_name) as arduino_port:
    print(arduino_port)
    while 1:
        read = arduino_port.readline().decode('utf-8')
        print(read)
        values = read.replace('{', '').replace('}', '').split(',')
        if values[0] == area:
            my_upload(values[0], values[1], values[2], values[3])
