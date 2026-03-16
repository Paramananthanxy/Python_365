import requests

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

response = requests.get(url)
if response.status_code != 200:
    print("API error")
r = response.json()

vuln = r.get('vulnerabilities')
print(type(vuln))


for item in vuln:
    cve_id = item['cve']['id']
    re = item['cve']['metrics']
    if 'cvssMetricV2' in re:
        
        v2_sev = re['cvssMetricV2'][0]['baseSeverity']
        v2_sc  = re['cvssMetricV2'][0]['impactScore']
        print("cvssMetricV2",cve_id,v2_sev,v2_sc)

    if 'cvssMetricV31' in re:
        v3_sev = re['cvssMetricV31'][0]['cvssData']['baseSeverity']
        v3_sc = re['cvssMetricV31'][0]['cvssData']['baseScore']
        print("cvssMetricv31--",cve_id,v3_sev,v3_sc)
    if 'cvssMetricV30' in re:
        v3_sev = re['cvssMetricV30'][0]['cvssData']['baseSeverity']
        v3_sec = re['cvssMetricV30'][0]['cvssData']['baseScore']
        print("cvssMetricV30--",cve_id,v3_sev,v3_sc)