import sqlite3

conn = sqlite3.connect('web.db')
cursor = conn.cursor()

cursor.execute("""SELECT id,published,descriptions FROM cve 
               WHERE lastmodified LIKE '1992-04-27T04:00:00.000' """)
print(cursor.fetchone())