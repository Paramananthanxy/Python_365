from flask import Flask


app = Flask(__name__)
@app.route("/user/<name>")
def user(name):
    names = "Hello "+name.title()
    return names


if __name__ == "__main__":
    app.run()