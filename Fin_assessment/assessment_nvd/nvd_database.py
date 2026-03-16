import sqlite3

def sql_connect():
    conn = sqlite3.connect('NVDs.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cve(
                   cve_id TEXT PRIMARY KEY,
                   descriptions TEXT,
                   published TEXT,
                   lastmodified TEXT,
                   basescore TEXT
                  ) """)
    conn.commit()

    return conn