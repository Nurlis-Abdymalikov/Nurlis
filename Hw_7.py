import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection
database_name = 'hw.db'

def create_table(connection, create_table_sgl):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sgl)
    except sqlite3.Error as e:
        print(e)


sql_to_create_product_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER NIT NULL DEFAULT 0
)
'''


my_connection = create_connection(database_name)
if my_connection is not None:
    print('Connection established')
    create_table(my_connection, sql_to_create_product_table)
    my_connection.close()

