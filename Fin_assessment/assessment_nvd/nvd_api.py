from flask import Flask,jsonify,render_template
from service import cve_id,spe_year,cve_score,cvlist
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/cve/list")
def cve_lists():
    data = cvlist()
    return jsonify(data)
@app.route("/cve/id/<id>")
def cve_ids(id):
    data = cve_id(id)
    return jsonify(data)

@app.route("/cve/year/<year>")
def cve_year(year):
    data = spe_year(year)
    return jsonify(data)

@app.route("/cve/scores/<id>")
def cve_scores(id):
    data = cve_score(id)
    return jsonify(data)

if __name__ == "__main__":
    app.run()