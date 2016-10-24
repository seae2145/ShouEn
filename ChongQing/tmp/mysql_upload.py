import datetime
import mysql.connector


def upload(area, objectID, objectName, objectValue):
    config = {
        'user': 'root',
        'password': 'lqdm)s6<;G-A',
        'host': 'localhost',
        'database': 'stipendiary',
    }

    # area = "999"
    # objectID = "0"
    # objectName = "0"
    # objectValue = "0"
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    insert_command = (
    "INSERT INTO `%s` (`ID`, `area`, `objectID`, `objectName`, `objectValue`, `date`, `time`) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', CURRENT_TIMESTAMP);" % (
    area, area, objectID, objectName, objectValue, date))

    cursor.execute(insert_command)

    cnx.commit()

    cursor.close()
    cnx.close()
