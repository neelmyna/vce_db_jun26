import pymysql

connection = pymysql.connect(user='root', password='Root123', host='localhost', port=3306, database='nithin_db', charset='utf8')
print('DB connected')
connection.close()
print('DB disConnected')