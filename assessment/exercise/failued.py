import requests
import xmltodict

url = 'https://jsonplaceholder.typicode.com/todos'

r = requests.get(url)
response = r.json()
filtered_data = []
for user in response:
    filtered = {
        'userId' : user['userId'],
        'task' : user['title'],
        'status': user['completed']
    }
    
    filtered_data.append(filtered)
    # print(filtered_data)
    filter_fail = []
for users in filtered_data:
    print(users)
    if users['status'] == False:
        # print(users)
        filter_fail.append(users)

# print(filter_fail)

data = {'users':{'user':filter_fail}}
xml_data = xmltodict.unparse(data,pretty = True)
# print(xml_data)


#api call
#store it as json
#store it in list
#filtering the data inside the list using loops
#using condition to filter the false status
#then store it in a list
# if we want to unparse in xmltodict we have to add root and store our list as item 
# in a variable 
#data = {'users':{'user':filtered_data}}
#then xml unparsing .. xmltodict.unparse(data,pretty=True) that's it 