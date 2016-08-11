import serial
import mssql_upload
import mysql_upload

# need change
port_name = "/dev/cu.usbmodem1421"

with serial.Serial(port_name) as arduino_port:
    print(arduino_port)
    while 1:
        readed = arduino_port.readline().decode('utf-8')
        print(readed)
        values = readed.replace('{', '').replace('}', '').split(',')
        mysql_upload.upload(values[0], values[1], values[2], values[3])
        mssql_upload.upload(values[0], values[1], values[2], values[3])