import csv
import sqlite3

conn = sqlite3.connect("wea.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS weath (
               date TEXT,
              temp INTEGER,
               humiditity FLOAT )""")
with open("C:/Python_Beg_to_Adv/assessment/api+sqli+csv/weather.csv",'r') as file:
    csv_file = csv.DictReader(file)


    for row in csv_file:
        cursor.execute("INSERT INTO weath (date,temp,humiditity) VALUES(?,?,?)",
            (row['Date'],row['Temperature_C'],row['Humidity_%'])
        )


conn.commit()
cursor.close()
conn.close()
