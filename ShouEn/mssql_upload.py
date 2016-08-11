import pymssql


def upload(area, objectID, objectName, objectValue):
    conn = pymssql.connect(server='192.168.0.20', user='sa', password='csii1qaz@WSX', database='stipendiary')

    cursor = conn.cursor()
    cursor.execute("INSERT INTO [dbo].[{}] (area, objectID, objectName, objectValue) VALUES (%s, %s, %s, %s)".format(area),
                   (area, objectID, objectName, objectValue))
    conn.commit()
    conn.close()
