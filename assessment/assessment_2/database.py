import sqlite3

db_name = 'weath.db'
def get_connect():
    return sqlite3.connect('weath.db')

def create_table():
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS weath(
                   date TEXT,
                   temp INTEGER,
                   humidity INTEGER,
                   pressure INTEGER )""")
    
    conn.commit()
    conn.close()
    

