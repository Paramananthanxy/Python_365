import requests 

url = 'https://randomuser.me/api/?results=10'

r = requests.get(url)
print(f"Status code: {r} ")
response_dict = r.json()
# print(response_dict['results'])


repo_di = response_dict['results']
re = repo_di[0]
print(f"the length {len(re)}")
print(f"The repositories : {len(repo_di)}")
names,
for users in repo_di:
    print(f"Name: {users['name']['first']}")
    print(f"Locaiton: {users['location']['city']}")
    print(f"Gender: {users['gender']}")
    # print(f"DOB : {int(dob)}")
    print(f"Email: {users['email']}")
    # print(keys)
