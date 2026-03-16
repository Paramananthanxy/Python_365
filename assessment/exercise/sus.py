import requests
import xmltodict

url = "https://jsonplaceholder.typicode.com/todos"
r = requests.get(url)
response = r.json()
filtered = []
failed_count = {}
for user in response:
    if user['completed'] == False:
        user_id = user['userId']
        if user_id in failed_count:
            failed_count[user_id] += 1
        else:
            failed_count[user_id] = 1
for key,value in failed_count.items():
    # print(key,value)
    if value > 10:
       fil={'userId':key,
            'failed_count':value}  
       filtered.append(fil)
data = {'users':{'user':filtered}}
xml_dict = xmltodict.unparse(data,pretty=True)

print(xml_dict)