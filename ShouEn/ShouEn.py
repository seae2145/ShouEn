import serial
from .mysql_upload import upload as my_upload
from .mssql_upload import upload as ms_upload

# need change
port_name = "/dev/ttyACM0"

with serial.Serial(port_name) as arduino_port:
    print(arduino_port)
    while 1:
        readed = arduino_port.readline().decode('utf-8')
        print(readed)
        values = readed.replace('{', '').replace('}', '').split(',')
        my_upload(values[0], values[1], values[2], values[3])
        ms_upload(values[0], values[1], values[2], values[3])
