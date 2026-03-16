from flask import Flask
import sqlite3



app = Flask(__name__)
@app.route("/wea/<date>")
def wea(date):
    conn = sqlite3.connect("C:/Python_Beg_to_Adv/assessment/api+sqli+csv/sqlite/wea.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weath WHERE date = ?",(date,))
    datt = cursor.fetchmany()
    conn.close()

    return str(datt)
if __name__ == "__main__":
    app.run()
