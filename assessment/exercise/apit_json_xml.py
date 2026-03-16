import requests
import xmltodict

url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url)
response = r.json()
data = {"users": {"user": response}}
print(response)
xml_file = xmltodict.unparse(data,pretty=True)
print(xml_file)
