import serial
from mysql_upload import upload as my_upload

# TODO Change Port Name for Windows
port_name = "/dev/cu.usbserial-A600K5I9"
area = str(301)

with serial.Serial(port_name) as arduino_port:
    print(arduino_port)
    while 1:
        try:
            read = arduino_port.readline().decode('utf-8')
            print(read)
            left_brace_location = read.index('{')
            right_brace_location = read.index('}')
            values = read[left_brace_location + 1:right_brace_location].split(',')
            print(values)
            if values[0] == area:
                my_upload(values[0], values[1], values[2], values[3])
        except:
            pass
