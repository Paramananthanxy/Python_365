from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route("/info")
def info():
    data={
 "name": "Param",
 "role": "Backend Developer",
 "language": "Python"
}
    return jsonify(data)

if __name__ == "__main__":
    app.run()