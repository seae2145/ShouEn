import mysql.connector

config = {
    'user': 'wmnl',
    'password': 'wmnl1691',
    'host': '163.13.129.21',
    'database': 'stipendiary',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT ID, area FROM stipendiary.`301` ORDER BY ID DESC LIMIT 1;")
query = ("SELECT ID FROM stipendiary.`301`;")
cursor.execute(query)

for i in cursor:
    print(i[1])

print(cursor.stored_results())
# for i in cursor.execute(query):
#     print(i)

# for i in cursor.stored_results():
#     print(i)

# print(cursor.stored_results())

cursor.close()
cnx.close()
