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

def create_db():
    database = input('Enter the database name to create it: ')
    query = f'create database if not exists {database}'
    connection = db_connect()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        db_disconnect(connection)
    except:
        print('Error while creating the DB')

def create_table():
    query = ''' create table if not exists books(
        id int primary key auto_increment,
        title varchar(100) not null,
        author varchar(100) not null,
        publisher varchar(100) not null,
        category varchar(32),
        number_of_pages smallint,
        price float default(100) check(price >= 100 and price <=10000)
    );'''
    connection = db_connect()
    try:
        cursor = connection.cursor()
        result = cursor.execute(query)
        print(f'Result = {result}')
        if result == 0:
            print('Table created successfully')
        else:
            print('Table already exists')
        cursor.close()
        db_disconnect(connection)
    except:
        print('Error while creating the table')

def read_book():
    title = input('Enter title of the book: ')
    author = input('Enter author of the book: ')
    publisher = input('Enter publisher of the book: ')
    category = input('Enter category of the book: ')
    number_of_pages = int(input('Enter number of pages of the book: '))
    price = float(input('Enter price of the book[100 to 10000]: '))
    return (title, author, publisher, category, number_of_pages, price)

def add_book(): # insert 1 row
    book = read_book()
    query = 'insert into books(title, author, publisher, category, number_of_pages, price) values(%s, %s, %s, %s, %s, %s)'
    connection = db_connect()
    try:
        cursor = connection.cursor()
        result = cursor.execute(query, book)
        connection.commit()
        print(f'Result = {result}')
        if result == 1:
            print('Row inserted successfully')
        else:
            print('Row insertion failed')
        cursor.close()
        db_disconnect(connection)
    except:
        print('Error while inserting row')

def delete_book(): # delete 1 row
    id = int(input('Enter Id of the book to delete: '))
    query = 'delete from books where id = %s'
    connection = db_connect()
    try:
        cursor = connection.cursor()
        result = cursor.execute(query, id)
        connection.commit()
        if result == 1:
            print('Row deleted successfully')
        else:
            print('Row deletion failed')
        cursor.close()
        db_disconnect(connection)
    except:
        print('Error while deleting row')

def update_book(): # update 1 row
    id = int(input('Enter Id of the book to update: '))
    price = float(input('Enter new price of the book: '))
    query = 'update books set price = %s where id = %s'
    connection = db_connect()
    try:
        cursor = connection.cursor()
        result = cursor.execute(query, (price, id))
        connection.commit()
        if result == 1:
            print(f'Book price with id = {id} updated to {price}')
        else:
            print(f'Book with id = {id} not found')
        cursor.close()
        db_disconnect(connection)
    except:
        print('Error while updating row')

def search_book(): # search using candidate key
    id = int(input('Enter Id of the book to search: '))
    query = 'select * from books where id = %s'
    connection = db_connect()
    try:
        cursor = connection.cursor()
        result = cursor.execute(query, id)
        if result == 1:
            book = cursor.fetchone()
            print(book)
        else:
            print(f'Book with id = {id} not found')
        cursor.close()
        db_disconnect(connection)
    except:
        print('Error while updating row')

def list_books(): # list all rows
    query = 'select * from books'
    connection = db_connect()
    try:
        cursor = connection.cursor()
        result = cursor.execute(query)
        print(f'Result = {result}')
        if result > 0:
            books = cursor.fetchall()
            print('-' * 105)
            print('%-2s %-22s %-15s %-18s %-20s %-15s  %s' %('ID', 'TITLE', 'AUTHOR', 'PUBLISHER', 'CATEGORY', 'NUMBER_OF_PAGES', 'PRICE'))
            print('-' * 105)
            for book in books:
                print('%-2d %-22s %-15s %-18s %-20s %15d  %06.1f' %(book[0], book[1], book[2], book[3], book[4], book[5], book[6]))
            print('-' * 105)
        else:
            print(f'No books were found')
        cursor.close()
        db_disconnect(connection)
    except:
        print('Error while updating row')

