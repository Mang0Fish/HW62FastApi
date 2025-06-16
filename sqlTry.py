import sqlite3
conn = sqlite3.connect('FirstDatabase.db') # connection to the db
conn.row_factory = sqlite3.Row # in order to use column name
cursor = conn.cursor()
cursor.execute('SELECT * FROM students') # send query
result = cursor.fetchall()
list_results = [tuple(row) for row in result]

for row in list_results:
    print(row)

list_data = [list(tup) for tup in list_results]
print(list_data)

'''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    signup_year INTEGER NOT NULL
'''
cursor.execute('''update students 
set birth = birth+1 
where is>- 1;''')
cursor.connection.commit()

conn.close()