import pymysql

def db_connect():
    connection = None
    try:
        connection = pymysql.connect(user='root', password='Root123', host='localhost', port=3306, database='nithin_db', charset='utf8')
        print('DB connected')
    except:
        print('Error while connecting to the DB')
    return connection

def db_disconnect(connection):
    try:
        connection.close()
        print('DB disConnected')
    except:
        print('Error while disconnecting the DB')
