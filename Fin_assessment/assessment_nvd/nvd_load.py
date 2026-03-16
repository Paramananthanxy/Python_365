import requests
from nvd_database import sql_connect
import time

def nvd_load():
    sql_connect()
    conn = sql_connect()
    cursor = conn.cursor()

    url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
    startindex = 0 
    resultperpage = 50

    while True:
        params = {
            'startIndex':startindex,
            'resultsPerPage':resultperpage
        }
        response = requests.get(url,params=params)
        time.sleep(1)
        if response.status_code !=200:
            print("API error:",response.status_code)
        r = response.json()
        
        vuln = r.get("vulnerabilities",[])
        for item in vuln:
            cve = item['cve']
            cve_id = cve['id']
            published = cve['published']
            descriptions = cve['descriptions'][0]['value']
            lastmodified = cve['lastModified']
            metric = cve['metrics']
            basescore = None
            if 'cvssMetricV2' in metric:
                basescore = metric['cvssMetricV2'][0]['cvssData']['baseScore']
            cursor.execute("""INSERT OR IGNORE INTO cve VALUES(?,?,?,?,?)""",(
                cve_id,descriptions,published,lastmodified,basescore
            ))
            conn.commit()
            startindex += 1
        if startindex >= 250:
            break
        

nvd_load()

