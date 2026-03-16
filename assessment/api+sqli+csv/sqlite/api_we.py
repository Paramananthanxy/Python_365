from flask import Flask,jsonify
import sqlite3


app = Flask(__name__)
@app.route("/weather/<date>")
def weather(date):
    conn = sqlite3.connect("C:/Python_Beg_to_Adv/assessment/api+sqli+csv/sqlite/weather1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather WHERE date = ?",(date,))
    out = cursor.fetchone()
    return jsonify({
        "date": out[0],
        "temperature":out[1],
        "Humidity":out[2],
        "WindSpeed":out[3]
    })

if __name__ == "__main__":
    app.run()
