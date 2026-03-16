import requests
import json

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

response = requests.get(url)
if response.status_code != 200:
    print(f"status code: {response.status_code}")
r = response.json()
# print(r.keys())
vulnerabilities = r.get('vulnerabilities',[])
print(type(vulnerabilities))
for vuln in vulnerabilities:
    re = vuln['cve']['metrics']
    # print(re)
    if 'cvssMetricV2' in re:
        print(re['cvssMetricV2'][0]['baseSeverity'])
        print(re['cvssMetricV2'][0]['cvssData']['baseScore'])
    