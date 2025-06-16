import sqlite3

conn: any = None
cursor: any = None
def connect(file_name: str) -> any:
    global conn, cursor
    conn = sqlite3.connect(file_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()


def run_query_select(query: str) ->[tuple]:
    cursor.execute(query)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    return result

def close():
    cursor.close()
def run_query_update(query: str) -> None:
    cursor.execute(query)
    cursor.connection.commit()

