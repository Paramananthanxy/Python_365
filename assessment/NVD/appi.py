from flask import Flask,jsonify
import sqlite3

app = Flask(__name__)
@app.route("/cve/<id>")
def cve(id):
    conn = sqlite3.connect('web.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT id,descriptions,published FROM cve WHERE id=?""",(id,))
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run()