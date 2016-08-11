import pymssql

conn = pymssql.connect(server='192.168.0.20', user='sa', password='csii1qaz@WSX', database='stipendiary')


def upload(area, objectID, objectName, objectValue):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO [dbo].[301] (area, objectID, objectName, objectValue) VALUES (%s, %s, %s, %s)",
                   (area, objectID, objectName, objectValue))
    conn.commit()
    conn.close()
