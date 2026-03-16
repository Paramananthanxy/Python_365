import sqlite3
import csv

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS weather ( data TEXT,
               temperature INTEGER,
               humidity INTEGER,
               windspeed FLOAT)
               """)
with open("C:/Python_Beg_to_Adv/assessment/api+sqli+csv/weather.csv",'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        cursor.execute("INSERT INTO weather VALUES (?,?,?,?)",
    (row['Date'],row['Temperature_C'],row['Humidity_%'],row['Wind_Speed_km_h'],))

conn.commit()
conn.close()

print("data loaded into database")