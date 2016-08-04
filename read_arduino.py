import serial

import list_serial_port

print(list_serial_port.serial_ports())

my_serial = serial.Serial(list_serial_port.serial_ports()[1])
print(my_serial.name)

while True:
    s = my_serial.readline().decode().strip('}\r\n').strip('{')
    print(s.split(','))
