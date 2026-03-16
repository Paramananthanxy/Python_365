from flask import Flask,jsonify
import sqlite3
import requests
from datetime import datetime,timedelta

#creating flask application
app = Flask(__name__)

#creating database 

conn = sqlite3.connect('cvee.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS cve 
               (cve_id TEXT PRIMARY KEY,
               description  TEXT,
               pulbished TEXT,
               last_modified TEXT)""")
conn.commit()


#GETTING THE DATA AND STORE IT IN DATABASE:

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

start_index = 0

while True:
    params = {
        "startIndex":start_index,
        "resultsPerPage":50
    }
    r = requests.get(url,params=params)
    data = r.json()
    start_index += 50
    # print(data)
    #seperating the json file 
    vulnerabilities = data.get("vulnerabilities",[])

    if not vulnerabilities:
        break

    for items in vulnerabilities:
    #  print(items.keys())
        cve = items['cve']
        id = cve['id']
        descriptions = cve['descriptions'][0]["value"]
        published = cve['published']
        lastmodified = cve['lastModified']
        
        cursor.execute("""INSERT OR IGNORE INTO cve VALUES (?,?,?,?)""",
                       (id,descriptions,published,lastmodified))
        conn.commit()
        start_index += 1
        print("Fetched:", start_index)

        if start_index > 200:
            break
conn.close()
    

    



