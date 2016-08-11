import pymssql
conn = pymssql.connect(server='192.168.0.20', user='sa', password='csii1qaz@WSX', database='stipendiary')

area = "301"
objectID = "502"
objectName = "TV"
objectValue = "On"


cursor = conn.cursor()
cursor.execute( "INSERT INTO [dbo].[301] (area, objectID, objectName, objectValue) VALUES (%s, %s, %s, %s)", (area, objectID, objectName, objectValue))
# c1 = conn.cursor()
# c1.execute('SELECT * FROM "301"')
# print( c1.fetchall() )  # shows result from c2 query!

conn.commit()
conn.close()
