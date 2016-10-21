import time
import mysql.connector

config = {
    'user': 'root',
    'password': 'lqdm)s6<;G-A',
    'host': 'localhost',
    'database': 'stipendiary',
}


def get_last_id(cursor):
    query = "SELECT ID, area, objectID, objectName, objectValue, time FROM stipendiary.`301` ORDER BY ID DESC LIMIT 1;"
    cursor.execute(query)
    cnx.commit()
    row = cursor.fetchone()
    if row is not None:
        last_id = row[0]
    else:
        last_id = 0
    return last_id


def get_data_from(cursor, id_number):
    query = ("SELECT ID, area, objectID, objectName, objectValue, time "
             "FROM stipendiary.`301` WHERE ID > {};".format(id_number))
    cursor.execute(query)
    return cursor


def main():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    last_id = get_last_id(cursor)
    print(last_id)
    while True:
        last_id = get_last_id(cursor)
        print(last_id)
        time.sleep(1)

    # while True:
    #     # cnx.commit()
    #     # query = ("SELECT ID, area, objectID, objectName, objectValue, time "
    #     #          "FROM stipendiary.`301` WHERE ID > {};".format(last_id))
    #     # cursor.execute(query)
    #     cursor = get_last_id(last_id)
    #     row = cursor.fetchone()
    #     while row is not None:
    #         print(row)
    #         last_id = row[0]
    #         row = cursor.fetchone()
    #
    #     time.sleep(1)
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()
