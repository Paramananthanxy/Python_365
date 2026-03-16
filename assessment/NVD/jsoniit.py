import requests
import json
import sqlite3
import time

conn = sqlite3.connect('web.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cve (
               id TEXT PRIMARY KEY,
               descriptions TEXT,
               published  TEXT,
               lastmodified TEXT)""")
conn.commit()

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
startindex = 0

while True:
    params = {
        'startIndex': startindex,
        'resultsPerPage' : 5
    }
    r = requests.get(url,params=params)
    time.sleep(1)
    if r.status_code != 200:
        print("API error:",r.status_code)
        break
    response = r.json()
    # print(json.dumps(response,indent=2))
    data = response.get('vulnerabilities',[])
    for item in data:
        cve = item['cve']
        id = cve['id']
        descriptions = cve['descriptions'][0]['value']
        lastmodified = cve['lastModified'] 
        published = cve['published']


        cursor.execute("""INSERT OR IGNORE INTO cve  VALUES(?,?,?,?) """,
                   (id,descriptions,lastmodified,published))

        conn.commit()
    startindex += 5
    if startindex > 200:
        break

