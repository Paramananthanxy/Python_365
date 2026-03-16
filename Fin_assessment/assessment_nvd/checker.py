import requests 
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
res = requests.get(url)
r = res.json()
vuln = r.get("vulnerabilities",[])
print(vuln[0]['cve'].keys())
# print(r.keys())
# print(type(r))
