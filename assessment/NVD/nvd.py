import requests
import sqlite3
from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# ---------------------------
# DATABASE SETUP
# ---------------------------

def create_database():

    conn = sqlite3.connect("cve.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cve (
        id TEXT PRIMARY KEY,
        description TEXT,
        published TEXT,
        last_modified TEXT
    )
    """)

    conn.commit()


# ---------------------------
# FETCH DATA FROM NVD API
# ---------------------------

def fetch_cve_data():

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    start_index = 0
    results_per_page = 50

    conn = sqlite3.connect("cve.db")
    cursor = conn.cursor()

    while True:

        params = {
            "startIndex": start_index,
            "resultsPerPage": results_per_page
        }

        response = requests.get(url, params=params)
        data = response.json()

        vulnerabilities = data.get("vulnerabilities", [])

        if not vulnerabilities:
            break

        for item in vulnerabilities:

            cve = item["cve"]

            cve_id = cve["id"]
            description = cve["descriptions"][0]["value"]
            published = cve["published"]
            modified = cve["lastModified"]

            cursor.execute("""
            INSERT OR IGNORE INTO cve VALUES (?, ?, ?, ?)
            """, (cve_id, description, published, modified))

        conn.commit()

        start_index += results_per_page
        print("Fetched:", start_index)

        if start_index > 200:
            break

    conn.close()


# ---------------------------
# API: GET CVE BY ID
# ---------------------------

@app.route("/cve/<cve_id>")

def get_cve(cve_id):

    conn = sqlite3.connect("cve.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cve WHERE id=?", (cve_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return jsonify(dict(result))

    return {"error": "CVE not found"}, 404


# ---------------------------
# API: GET RECENT CVE
# ---------------------------

@app.route("/cve/recent/<days>")

def recent_cves(days):

    conn = sqlite3.connect("cve.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    date_limit = datetime.utcnow() - timedelta(days=int(days))

    cursor.execute("""
    SELECT * FROM cve
    WHERE last_modified >= ?
    """, (date_limit.isoformat(),))

    results = cursor.fetchall()

    conn.close()

    return jsonify([dict(row) for row in results])


# ---------------------------
# MAIN PROGRAM
# ---------------------------

if __name__ == "__main__":

    print("Creating database...")
    create_database()

    print("Fetching CVE data from NVD API...")
    fetch_cve_data()

    print("Starting API server...")
    app.run(debug=True)