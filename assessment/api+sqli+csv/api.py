from flask import Flask
import sqlite3

app=Flask(__name__)

@app.route("/weather/<date>")
def get_weather(date):

    conn = sqlite3.connect("C:/Python_Beg_to_Adv/assessment/api+sqli+csv/wea.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weather WHERE data = ?",(date,))
    result = cursor.fetchone()
    conn.close()
    return str(result)
app.run()