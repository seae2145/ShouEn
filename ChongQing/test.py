from ChongQing.mysql_upload import upload as my_upload

# TODO Change Port Name for Windows
port_name = "/dev/cu.usbserial-A600K5I9"
# my_upload('301', 'a01', '100', '50')
# living room
my_upload('301', '1501', 'gateway', 'sleep')
my_upload('301', '1401', 'test', '46')
my_upload('301', '1001', 'test', 'On')
my_upload('301', '601', 'test', 'Off')
# bathroom
my_upload('301', '302', 'test', 'On')
my_upload('301', '602', 'test', 'On')
my_upload('301', '402', 'test', '60')
my_upload('301', '402', 'test', '60')
my_upload('301', '401', 'test', '60')
my_upload('301', '401', 'test', '60')
my_upload('301', '302', 'test', 'Off')
my_upload('301', '602', 'test', 'Off')
my_upload('301', '401', 'test', '60')
my_upload('301', '401', 'test', '60')
# guest room
my_upload('301', '2001', 'test', 'Taken')
my_upload('301', 'a01', '140', '95')
my_upload('301', '901', 'power', 'on')
my_upload('301', '901', 'channel', '35')
my_upload('301', '901', 'channel', '69')
my_upload('301', '901', 'volume', 'up')
my_upload('301', '901', 'volume', 'down')
# 廚房
my_upload('301', '303', 'test', 'On')
my_upload('301', '603', 'test', 'On')
my_upload('301', '503', 'test', 'On')
my_upload('301', '503', 'test', 'Off')
my_upload('301', '404', 'test', '60')
my_upload('301', '404', 'test', '60')
my_upload('301', '604', 'test', 'On')
my_upload('301', '502', 'test', 'On')
my_upload('301', '502', 'test', 'Off')
my_upload('301', '303', 'test', 'Off')
my_upload('301', '603', 'test', 'Off')
#
# TODO 落地燈？
my_upload('301', '504', 'test', 'On')
