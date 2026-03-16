from nvd_db import connect
import requests
import time 

def load():
    connect()
    conn = connect()
    cursor = conn.cursor()

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    startindex = 0 

    while True:
     params = {
        "startIndex":startindex,
        "resultsPerPage":20
     }
     response = requests.get(url,params=params)
     if response.status_code != 200:
        print(f"API error : {response.status_code}")
     r = response.json()
     time.sleep(1)
     vulnerabilities = r.get("vulnerabilities",[])
     for items in vulnerabilities:
        cve =items['cve']
        id = cve['id']
        descriptions = cve['descriptions'][0]['value']
        published = cve['published']
        lastmodified = cve['lastModified']




        cursor.execute("""INSERT OR IGNORE INTO cve VALUES (?,?,?,?)""",
                       (id,descriptions,published,lastmodified))
        conn.commit()
        startindex +=1
        if startindex  > 200:
           break
load()