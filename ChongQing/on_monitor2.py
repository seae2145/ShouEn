import time
import mysql.connector

config = {
    'user': 'root',
    'password': 'lqdm)s6<;G-A',
    'host': 'localhost',
    'database': 'stipendiary',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


def get_last_id():
    query = "SELECT ID, area, objectID, objectName, objectValue, time FROM stipendiary.`301` ORDER BY ID DESC LIMIT 1;"
    cursor.execute(query)
    row = cursor.fetchone()
    if row is not None:
        last_id = row[0]
    else:
        last_id = 0
    return last_id

last_id = get_last_id()

while True:
    cnx.commit()
    query = ("SELECT ID, area, objectID, objectName, objectValue, time "
             "FROM stipendiary.`301` WHERE ID > {};".format(last_id))
    cursor.execute(query)


    row = cursor.fetchone()
    while row is not None:
        print(row)
        last_id = row[0]
        row = cursor.fetchone()

    time.sleep(1)

cursor.close()
cnx.close()
