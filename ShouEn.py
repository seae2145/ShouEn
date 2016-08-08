import serial
import mysql_test2

# need change
port_name = "/dev/cu.usbmodem1421"
with serial.Serial(port_name) as arduino_port:
    print(arduino_port)
    while 1:
        readed = arduino_port.readline().decode('utf-8')
        print(readed)
        values = readed.replace('{', '').replace('}', '').split(',')
        for i in values:
            print(i)
        mysql_test2.upload(values[0], values[1], values[2], values[3])