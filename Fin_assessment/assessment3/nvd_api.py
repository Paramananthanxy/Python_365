from flask import Flask,jsonify
from service import cve_id,nvd_lastmodifi

app = Flask(__name__)

@app.route("/cve/<id>")
def cve(id):
    data = cve_id(id)
    return jsonify(data)

@app.route("/lastmodified/<days>")
def lastmodified(days):
    data = nvd_lastmodifi(days)
    return jsonify(data)


if __name__=="__main__":
    app.run()

