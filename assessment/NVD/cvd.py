from flask import Flask,jsonify
import sqlite3
import requests
import json


app = Flask(__name__)
#create table 

conn = sqlite3.connect('cvee.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cve (
               id TEXT PRIMARY KEY,
               description TEXT,
               published TEXT,
               lastmodified TEXT)""")
conn.commit()

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

start_index = 0

while True:
    params = {
        'startIndex':start_index,
        'resultsPerPage':20
    }
    response = requests.get(url,params=params)
    r = response.json()
    print(r.keys())
    # vulnerabilities =r.get("vulnerabilities",[])
    # for cve in vulnerabilities:
    #     item = cve['cve']
    #     id = item['id']
    #     published = item['published']
    #     descriptions = item['descriptions'][0]['value']
    #     lastmodified = item['lastModified']
    #     print(descriptions)
    # start_index += 20

    if start_index > 40:
        break
