import mysql.connector

config = {
    'user': 'wmnl',
    'password': 'wmnl1691',
    'host': '163.13.129.21',
    'database': 'stipendiary',
}


def last_id():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = "SELECT ID, area, objectID, objectName, objectValue, time FROM stipendiary.`301` ORDER BY ID DESC LIMIT 1;"
    cursor.execute(query)

    row = cursor.fetchone()
    if row is not None:
        return row[0]
    else:
        return 0

    cursor.close()
    cnx.close()


def check_new_data(from_id):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = ("SELECT ID, area, objectID, objectName, objectValue, time "
             "FROM stipendiary.`301` WHERE ID > {};".format(from_id))
    cursor.execute(query)
    # cursor.execute(query, 0)
    # cursor.execute(query)

    row = cursor.fetchone()
    while row is not None:
        print(row[0])
        row = cursor.fetchone()

    cursor.close()
    cnx.close()
    # for i in cursor:
    #     print(i[1])
    #
    # print(cursor.stored_results())
    # for i in cursor.execute(query):
    #     print(i)

    # for i in cursor.stored_results():
    #     print(i)

    # print(cursor.stored_results())



    # query = ("SELECT ID, area FROM stipendiary.`301` ORDER BY ID DESC LIMIT 1;")
    #     query = ("SELECT ID FROM stipendiary.`301`;")

if __name__ == '__main__':
    last_id()
    check_new_data(28400)
