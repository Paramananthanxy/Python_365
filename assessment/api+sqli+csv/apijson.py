from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/weather')
def weather():
    data = {
        "temperature":23,
        "humidity":59
    }
    return jsonify(data)
app.run()

