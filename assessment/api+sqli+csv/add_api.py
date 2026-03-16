from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/add/<num1>/<num2>")
def add(num1,num2):
    num = int(num1) + int(num2)
    numm = str(num)
    return jsonify({"sum":numm})
if __name__ == "__main__":
    app.run()
