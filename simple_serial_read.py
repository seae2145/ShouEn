import serial

s = "/dev/cu.usbserial-A9007KEk"
test = serial.Serial(s)
print(test)
# with serial.Serial(s) as ser:
#     print(ser)
    # while 1:
    #
    #     print(ser.readline().decode('utf-8'))
