import time
from ChongQing.pushy import PushyAPI
import mysql.connector

config = {
    'user': 'root',
    'password': 'lqdm)s6<;G-A',
    'host': 'localhost',
    'database': 'stipendiary',
}
number_dict = {
    '301': '臥室紅外線', '302': '浴室紅外線', '303': '廚房紅外線', '304': '客廳紅外線',
    '401': '洗手槽水龍頭流速', '402': '馬桶水箱流速', '403': '洗手槽水龍頭流速', '404': '洗手槽水龍頭流速',
    '501': '浴室門', '502': '冰箱門', '503': '廚櫃門', '504': '玄關門',
    '601': '燈', '602': '燈', '603': '燈', '604': '電磁爐', '605': '燈',
    '1001': '窗簾',
    '1401': '紅外線發射器',
    '2001': '智慧藥盒',
    'a01': '血壓計',
}
status_dict = {
    'Open': '開', 'Close': '關',
    'On': '開', 'Off': '關',
    'on': '開', 'off': '關', 'stop': '停止',
    'Taken': '吃藥',
}
ir_status = {
    'On': '有人', 'Off': '無人',
}
remote_control_dict = {
    '01': '電視開關鍵', '02': '電視頻道向上', '03': '電視頻道向下', '04': '電視音量調大', '05': '電視音量調小', '06': '電視頻道1',
    '07': '電視頻道2', '08': '電視頻道3', '09': '電視頻道4', '10': '電視頻道5', '11': '電視頻道6', '12': '電視頻道7',
    '13': '電視頻道8', '14': '電視頻道9', '15': '電視頻道0', '16': '電視返回鍵', '17': '電視靜音鍵', '18': '電視輸入切換鍵',
    '19': '上鍵', '20': '下鍵', '21': '左鍵', '22': '右鍵', '23': 'OK',
    '24': '冷氣開,溫度25,風量中',
    '25': '冷氣開,溫度18,風量小',
    '26': '冷氣開,溫度19,風量小',
    '27': '冷氣開,溫度20,風量小',
    '28': '冷氣開,溫度21,風量小',
    '29': '冷氣開,溫度22,風量小',
    '30': '冷氣開,溫度23,風量小',
    '31': '冷氣開,溫度24,風量小',
    '32': '冷氣開,溫度25,風量小',
    '33': '冷氣開,溫度26,風量小',
    '34': '冷氣開,溫度27,風量小',
    '35': '冷氣開,溫度28,風量小',
    '36': '冷氣開,溫度18,風量中',
    '37': '冷氣開,溫度19,風量中',
    '38': '冷氣開,溫度20,風量中',
    '39': '冷氣開,溫度21,風量中',
    '40': '冷氣開,溫度22,風量中',
    '41': '冷氣開,溫度23,風量中',
    '42': '冷氣開,溫度24,風量中',
    '43': '冷氣開,溫度25,風量中',
    '44': '冷氣開,溫度26,風量中',
    '45': '冷氣開,溫度27,風量中',
    '46': '冷氣開,溫度28,風量中',
    '47': '冷氣開,溫度18,風量強',
    '48': '冷氣開,溫度19,風量強',
    '49': '冷氣開,溫度20,風量強',
    '50': '冷氣開,溫度21,風量強',
    '51': '冷氣開,溫度22,風量強',
    '52': '冷氣開,溫度23,風量強',
    '53': '冷氣開,溫度24,風量強',
    '54': '冷氣開,溫度25,風量強',
    '55': '冷氣開,溫度26,風量強',
    '56': '冷氣開,溫度27,風量強',
    '57': '冷氣開,溫度28,風量強',
    '58': '冷氣睡眠,溫度26,自動',
    '59': '冷氣關',
}


def new_data_query(id_from):
    return ("SELECT ID, area, objectID, objectName, objectValue, time "
            "FROM stipendiary.`301` WHERE ID > {};".format(id_from))


def status_trans(sensor_number, status_string, status_string2):
    if sensor_number[0] == '3':
        return ir_status[status_string]
    elif sensor_number[0] == '4':
        return status_string
    elif sensor_number[0] == 'a':
        if status_string2 > 140 or status_string > 80:
            # Payload data you want to send to devices
            data = {'message': '血壓過高'}
            # The recipient device registration IDs
            registration_ids = ['6ed6292be4ac96e7b68e9e']  # TODO 改
            # Send the push notification with Pushy
            PushyAPI.sendPushNotification(data, registration_ids)
        return '收縮壓：' + str(status_string2) + '舒張壓：' + str(status_string)
    else:
        return status_dict[status_string]


last_id = 0
last_id_query = "SELECT ID FROM `301` ORDER BY ID DESC LIMIT 1;"

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

cursor.execute(last_id_query)
row = cursor.fetchone()
if row is not None:
    last_id = row[0]

print(last_id)
cnx.commit()

while True:
    try:
        cursor.execute(new_data_query(last_id))
        row = cursor.fetchone()
        while row is not None:
            last_id = row[0]
            print(row)
            model = number_dict[row[2]]
            status = status_trans(row[2], row[4], row[3])
            sensor_time = row[5].strftime('%H:%M:%S')
            print(model, ':', status, '\t', sensor_time)
            row = cursor.fetchone()
        cnx.commit()
        time.sleep(1)
    except:
        pass

cursor.close()
cnx.close()
