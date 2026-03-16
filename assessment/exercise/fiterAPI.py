#API
# ↓
#requests.get()
# ↓
#JSON
# ↓
#Python list/dictionary
# ↓
#filter useful fields
# ↓
#build new structure
# ↓
#xmltodict.unparse()
# ↓
#XML output
import requests
import xmltodict

url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url)
response = r.json()

filtered = {}
filtered_user = []
for key in response:
    filtered ={
     'name' : key['name'],
     'email' : key['email'],
     'city' : key['address']['city']
    }
    filtered_user.append(filtered)
  
   
# print(filtered_user)

data = {'users':{'user':filtered_user}}

xml_dict = xmltodict.unparse(data,pretty=True)

print(xml_dict)
