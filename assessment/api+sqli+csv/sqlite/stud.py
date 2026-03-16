import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
               id INTEGER,
               name TEXT,
               age INTEGER )""")
data = [(1, 'Randy', 23),
(2, 'John', 25),
(3, 'David', 21),
(4, 'Lisa', 24),
(5, 'Emma', 22),
(5, "Emma", 22),
(6, "Mark", 27),
(7, "Sophia", 20),
(8, "Daniel", 26)]

cursor.executemany("INSERT INTO student (id,name,age) VALUES(?,?,?)",data )


conn.commit()
for item in cursor.execute("SELECT * FROM student WHERE age > 22"):

    # item = cursor.fetchone()
    print(item)
cursor.close()
conn.close()

