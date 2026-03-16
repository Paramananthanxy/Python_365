#Conditional Tests

#5.1 

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#5.2
name1 = "Akaza"
name2 = "akaza"
if name1 == name2 :
    print("same")
else:
    print("not same ")

#5.3 Alien Colors #1 && 5.4  #2 &&5.5 #3
alien_col = 'yellow'
alien_color =['green','yellow','red']
if alien_col in alien_color:
    print('You earned 5 points')
else:
    print("10 points ")

#5.6 Stages of life 
age = 23

if age < 2:
    print("the person is a baby")
elif age < 4 :
    print("Toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("adult")
elif age > 65 :
    print("Elder")

#5.6 Favorite Fruite:
favorite_fruits = ['apple','banana','cherry','domas']
if 'cherry' in favorite_fruits:
    print('this is my favorite fruite')
else:
    print("this is not my favoirte fruite")

#5.8 Hello admin:
username = ['user','loser','admin','randy']
for user in username:
    if user == 'admin':
        print("Welcom admin")
        print("Would you like to see the status report ?...")
    else :
        print("Hello",user)
        print("\n thank for you loging in again")

#5.10 checking username
current_users = ['randy','rambo','roman','rock']
new_users =['rock','ceser','jesus','alla','roman']

for new in new_users:
    if new in current_users:
        print("the name is already taken",new)
    else:
        print("\n This name is available....",new )

#5.11 ordinal Numbers:
a = [a for a in range(1,10) ]
print(a)
for x in a:
    if x ==1:
        print(str(x)+"st")
    elif x ==2:
       print(str(x)+"nd")
    elif x ==3:
       print(str(x)+"rd")
    else:
        print(str(x)+"th")
