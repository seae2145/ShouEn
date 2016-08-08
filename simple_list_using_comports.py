import serial.tools.list_ports

s = serial.tools.list_ports.comports()
for i in s:
    print(i.device)
