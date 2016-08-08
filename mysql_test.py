import mysql.connector
import sys, os

user = 'test'
pwd = 'test'
host = '163.13.128.72'
db = 'test'
table = '301'

Account = "1"
Password = "2"

# insert_sql = "INSERT INTO %s(Account,Password)VALUES ('%s','%s')" % (table, Account, Password)
# insert_sql = "INSERT INTO 301(area, objectID, objectName, objectValue, date)VALUES ('%s','%s','%s','%s')" % (1, 2, 3, 4)
# insert_sql = "INSERT INTO 301(area, objectID, objectName, objectValue, date)VALUES (1,2,3,4)"
select_sql = "SELECT id  FROM %s" % table

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()

# try:
#     cursor.execute(insert_sql)
# except mysql.connector.Error as err:
#     print("insert table 'mytable' faild.")
#     print("Error: {}".format(err.msg))
#     sys.exit()

try:
    cursor.execute(select_sql)
    for (id, Account, Password) in cursor:
        print("id:{} Account:{} Password:{}".format(id, Account, Password))


except mysql.connector.Error as err:
    print("query table 'mytable' failed.")
    print("Error:{}".format(err.msg))
    sys.exit()

cnx.commit()
cursor.close()
cnx.close()
