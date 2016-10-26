import time
import datetime
import mysql.connector
from ChongQing.pushy import PushyAPI
from ChongQing.libs.dicts import *

config = {
    'user': 'stipendiary',
    'password': '073109383',
    'host': 'localhost',
    'database': 'stipendiary',
}
is_302_no_man = None
is_303_no_man = None
is_604_on = None


def get_last_id(cnx):
    cursor = cnx.cursor()
    query = "SELECT ID FROM `301` ORDER BY ID DESC LIMIT 1;"
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    cnx.commit()
    if row is None:
        return 0
    else:
        return row[0]


def get_new_data(cnx, from_number):
    cursor = cnx.cursor()
    query = "SELECT ID, objectID, objectName, objectValue, time FROM `301` WHERE ID > {};".format(from_number)
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    cnx.commit()
    return row


def print_on_monitor(object_id, object_name, object_value, trigger_time):
    sensor_name = number_dict[object_id]
    sensor_time = trigger_time.strftime('%H:%M:%S')

    if object_id[0] == '3':
        sensor_status = status_dict_ir[object_value]
        global is_303_no_man
        global is_604_on
        if object_id == '302':
            change_man_in_302(object_value)
        if object_id == '303':
            change_man_in_303(object_value)
            if is_604_on and is_303_no_man:
                print(datetime.datetime.now().strftime('%H:%M:%S') + '   發送通知長輩電磁爐沒關')
                push_note('電磁爐沒關')
                is_303_no_man = False

    elif object_id[0] == '4':
        sensor_status = object_value
        global is_302_no_man
        if object_id == '401' and is_302_no_man:
            print(datetime.datetime.now().strftime('%H:%M:%S') + '   發送通知長輩洗手台水沒關')
            push_note('水龍頭沒關')
            is_302_no_man = False

    elif object_id[0] == '6':
        sensor_status = status_dict[object_value]
        if object_id == '604':
            change_604_onoff(object_value)

    elif object_id[0] == '9':
        sensor_status = status_for_901(object_name, object_value)

    elif object_id[0] == 'a':
        sensor_status = status_for_a01(object_name, object_value)
        if int(object_name) > 140 or int(object_value) > 80:
            print(datetime.datetime.now().strftime('%H:%M:%S') + '   發送通知家屬血壓過高')
            push_note('血壓過高')
    else:
        sensor_status = status_dict[object_value]

    print(sensor_time + '   ' + sensor_name + '：' + sensor_status)


def status_for_901(object_name, object_value):
    status = ''
    if object_name == 'power':
        status = status_dict[object_value]
    elif object_name == 'channel':
        status = object_value
    elif object_name == 'mute':
        status = ''
    elif object_name == 'volume':
        status = status_dict[object_value]
    status_prefix = status_prefix_dict[object_name]
    return status_prefix + status


def status_for_a01(object_name, object_value):
    status = '收縮壓：' + object_name + ' 舒張壓：' + object_value
    return status


def change_man_in_302(status):
    global is_302_no_man
    if status == 'On':
        is_302_no_man = False
    elif status == 'Off':
        is_302_no_man = True


def change_man_in_303(status):
    global is_303_no_man
    if status == 'On':
        is_303_no_man = False
    elif status == 'Off':
        is_303_no_man = True


def change_604_onoff(status):
    global is_604_on
    if status == 'On':
        is_604_on = True
    elif status == 'Off':
        is_604_on = False


def push_note(message):
    # Payload data you want to send to devices
    data = {'message': message}
    # The recipient device registration IDs
    registration_ids = ['418720f46bb10272ec7d0d']  # TODO 改
    # Send the push notification with Pushy
    PushyAPI.sendPushNotification(data, registration_ids)


def main():
    cnx = mysql.connector.connect(**config)
    last_id = get_last_id(cnx)
    while True:
        new_datas = get_new_data(cnx, last_id)
        # new_datas = get_new_data(cnx, 10000)
        if new_datas:
            for table_id, objectID, objectName, objectValue, trigger_time in new_datas:
                print_on_monitor(objectID, objectName, objectValue, trigger_time)
            last_id = new_datas[-1][0]


if __name__ == '__main__':
    main()
