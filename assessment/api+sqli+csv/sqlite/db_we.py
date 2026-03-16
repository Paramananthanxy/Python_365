import csv
import sqlite3

conn = sqlite3.connect("weather1.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS  weather(
               date TEXT,
               temperature INTEGER,
               humidity INTEGER,
               windspeed INTEGER)""")
with open("C:/Python_Beg_to_Adv/assessment/api+sqli+csv/sqlite/weather1.csv",'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        cursor.execute("INSERT INTO weather (date,temperature,humidity,windspeed) VALUES(?,?,?,?)",
                       (row['Date'],row['Temperature'],row['Humidity'],row['WindSpeed']))
        
conn.commit()
cursor.close()
