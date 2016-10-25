import time
import mysql.connector

config = {
    'user': 'root',
    'password': 'lqdm)s6<;G-A',
    'host': 'localhost',
    'database': 'stipendiary',
}

last_id = 0
cnx = mysql.connector.connect(**config)

while True:
    cursor = cnx.cursor()
    query = "SELECT ID FROM `301` ORDER BY ID DESC LIMIT 1;"
    cursor.execute(query)
    row = cursor.fetchone()
    print(row[0])
    # cnx.commit()
    cursor.close()
    time.sleep(1)

cnx.close()
