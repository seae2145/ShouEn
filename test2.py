import serial

port_name = "/dev/cu.usbserial-A600K5I9"


with serial.Serial(port_name) as arduino_port:
    print(arduino_port)
    while 1:
        read = arduino_port.readline().decode('utf-8')
        print(read)
        values = read[1:-3].split(',')  # Delete '{' and '}\r\n'
        print(values)

