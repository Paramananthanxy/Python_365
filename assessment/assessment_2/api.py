from flask import Flask
from service import get_weather,get_year

app = Flask(__name__)

@app.route("/weather/<date>")
def weather(date):
    r = get_weather(date)
    return r 

@app.route("/stat/<year>")
def stat(year):
    r = get_year(year)
    return r 

if __name__ == '__main__':
    app.run() 