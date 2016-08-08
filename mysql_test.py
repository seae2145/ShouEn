# import mysql.connector
#
# cnx = mysql.connector.connect(user='test', password='test',
#                               host='163.13.128.72',
#                               database='test')
# cnx.close()

import mysql.connector
import sys, os

user = 'test'
pwd = 'test'
host = '163.13.128.72'
db = 'test'

Account = "fuck"
Password = "fuuuuck"

insert_sql = "INSERT INTO studenttest(Account,Password)VALUES ('%s','%s')" % (Account, Password)
select_sql = "SELECT id , Account , Password FROM studenttest"

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()

try:
    cursor.execute(insert_sql)
except mysql.connector.Error as err:
    print("insert table 'mytable' faild.")
    print("Error: {}".format(err.msg))
    sys.exit()

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
