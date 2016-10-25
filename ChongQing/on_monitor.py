import time
import mysql.connector
from ChongQing.pushy import PushyAPI
from ChongQing.libs.dicts import *

config = {
    'user': 'root',
    'password': 'lqdm)s6<;G-A',
    'host': 'localhost',
    'database': 'stipendiary',
}

status_302 = None
status_303 = None


def push_note(message):
    # Payload data you want to send to devices
    data = {'message': message}
    # The recipient device registration IDs
    registration_ids = ['6ed6292be4ac96e7b68e9e']  # TODO 改
    # Send the push notification with Pushy
    PushyAPI.sendPushNotification(data, registration_ids)


def new_data_query(id_from):
    return ("SELECT ID, area, objectID, objectName, objectValue, time "
            "FROM stipendiary.`301` WHERE ID > {};".format(id_from))


def status_trans(sensor_number, row4, row3):
    if sensor_number[0] == '3':
        return status_dict_ir[row4]
    elif sensor_number[0] == '4':
        return row4
    elif sensor_number[0] == '9':
        if row3 == 'channel':
            return status_prefix_dict[row3] + str(row4)
        else:
            return status_prefix_dict[row3] + status_dict[row4]
    elif sensor_number[0] == 'a':
        if row3 > 140 or row4 > 80:
            push_note('血壓過高')
        return '收縮壓：' + str(row3) + '舒張壓：' + str(row4)
    else:
        return status_dict[row4]


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
            # 水流通知
            if row[2] == '302':
                status_302 = row[4]
            elif row[2] == '401' and status_302 == 'Off':
                push_note('水流忘記關')
            # 瓦斯通知
            if row[2] == '303':
                status_302 = row[4]
            elif row[2] == '604' and status_303 == 'Off':
                push_note('電磁爐忘記關')

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
