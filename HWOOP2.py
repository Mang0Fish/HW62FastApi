import sqlite3
from Customer import Customer

connection = sqlite3.connect("customers.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    address TEXT NOT NULL,
    mobile TEXT NOT NULL
    );
    ''')

# cursor.execute('''
# INSERT INTO customers VALUES
#
#     (1, 'John', 'Doe', 'USA', '050'),
#     (2, 'Jane', 'Smith', 'France', '051'),
#     (3, 'Alice', 'Johnson', 'Germany', '052'),
#     (4, 'Bob', 'Brown', 'Spain', '053'),
#     (5, 'Charlie', 'Davis', 'Italy', '054')
# ''')
#
# connection.commit()


def print_all_customers():
    cursor.execute('''
    SELECT * FROM customers
        ''')
    for row in cursor.fetchall():
        print(tuple(row))

def insert_customer(c: Customer):
    cursor.execute(f'''
    INSERT INTO customers VALUES
    ({c.id}, '{c.fname}', '{c.lname}', '{c.address}', '{c.mobile}')
    ''')
    connection.commit()

c1 = Customer(6, "Ali", "Baba", 'Persia', '501234567')

print_all_customers()
insert_customer(c1)
print_all_customers()



connection.close()
