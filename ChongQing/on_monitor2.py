import mysql.connector

config = {
    'user': 'stipendiary',
    'password': '073109383',
    'host': '163.13.129.28',
    'database': 'stipendiary',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = "SELECT ID, area, objectID, objectName, objectValue, time FROM stipendiary.`301` ORDER BY ID DESC LIMIT 1;"
cursor.execute(query)

row = cursor.fetchone()
if row is not None:
    last_id = row[0]
else:
    last_id = 0

while True:
    query = ("SELECT ID, area, objectID, objectName, objectValue, time "
             "FROM stipendiary.`301` WHERE ID > {};".format(last_id))
    cursor.execute(query)

    row = cursor.fetchone()
    while row is not None:
        print(row[0])
        row = cursor.fetchone()

cursor.close()
cnx.close()
