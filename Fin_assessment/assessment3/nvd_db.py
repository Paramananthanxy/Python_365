import sqlite3

def connect():
    conn = sqlite3.connect('nvd.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS cve(
               id TEXT PRIMARY KEY,
                descriptions TEXT,
                published TEXT,
                lastmodified TEXT)""")
    
    conn.commit()
    return conn
connect()