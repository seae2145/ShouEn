import datetime
import mysql.connector


def upload(area, objectID, objectName, objectValue):
    config = {
        'user': 'wmnl',
        'password': 'wmnl1691',
        'host': '163.13.129.21',
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
    "INSERT INTO `301` (`ID`, `area`, `objectID`, `objectName`, `objectValue`, `date`, `time`) VALUES (NULL, '%s', '2', '3', '49999', '%s', CURRENT_TIMESTAMP);" % (
    area, date))

    cursor.execute(insert_command)

    cnx.commit()

    cursor.close()
    cnx.close()
