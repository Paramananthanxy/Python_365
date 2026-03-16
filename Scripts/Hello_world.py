# print("Hello World!")

# #even number using range 
# i = list(range(2,13,2))
# print(i)

# square = []
# for value in range(1,11):
#     value = value**2
#     square.append(value)
# print(square)

# #List comprehension
# Squares = [values**2 for values in range(1,20,2)]
# print(Squares)

# #slicing a list 
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:3])

# #Looping through a slice 

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())


# alien = {'color':'green'}
# print(alien['color'])

# alien = {'color':'green'}
# print(alien)

# # adding new key and value in the dictonary 
# alien['x_position'] = 0
# alien['y_position'] = 25

# print(alien)

# players[0] ='allen'
# print(players)


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# print("Original x-position: " + str(alien_0['x_position']))

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#  x_increment = 1
 
#  print("New x-position: " + str(alien_0['x_position']))
# elif alien_0['speed'] == 'medium':
 
#  x_increment = 2
#  print("New x-position: " + str(alien_0['x_position']))
# else:
#  # This must be a fast alien.

#  x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))

# #looping in dictionary

# user = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }

# for key,value in user.items():
#   print("\n key :"+key)
#   print("value : "+value)



#   #Nested aliens 

#   aliens = []

#   for alien in range(30):
#     new_alien = {
#       'color':'green'
#       ,'point':'5'
#     }
#     aliens.append(new_alien)

#     for alien in aliens[1:6]:
#         print(alien)
#         print(".....")
# print("Total number of aliens"+str(len(aliens)))

# fav_lang = {
#   'jen': ['python', 'ruby'],
#  'sarah': ['c'],
#  'edward': ['ruby', 'go'],
#  'phil': ['python', 'haskell'],
# }

# for name,language in fav_lang.items():
#   print("\n The fav lang of ",name)
#   for languages in language:
#     print("\t",languages)


# #while loop 

# # prompt = "\nTell me something, and I will repeat it back to you:"
# # prompt += "\nEnter 'quit' to end the program. "
# # message = "qu"
# # # while message != 'quit':
# # #  message = input(prompt)
# # #  print(message)


# #  #while loop using flags 
# # active = True
# # while active:
# #    mesage = input(prompt)
# #    if message =='quit':
# #      active = False
# #    else:
# #      print(message)  

# # num = int(input("Enter the number "))
# # while num < 10:
# #   num+=1
# #   if num % 2 == 0:
# #     continue
# #   print(num)
# # else:
# #      print(num ,"Invalid numbers")


# unverified_users = ['alice','bran','Emiliy']

# verified_user = []

# while unverified_users:
#   users = unverified_users.pop()
#   print("Verified user"+users.title())
#   verified_user.append(users)

# for verified_users in verified_user:
#     print("The verified user are : "+verified_users)


# #Filling a Dictionary with User input:
# responses = {}

# polling = True

# while polling:
#   name = input("Enter your name :")
#   response = input("Which moutain do you want to climb :")

#   responses[name]=response
#   print(responses)
#   resp = input("if you want to continue this polling type 'yes'/ 'no'")
#   if resp == 'no':
#     polling = False
# for name,response in responses.items():
#   print(name,"the faviourate moutain to climb is :",response) 



# ###funciton
# def greet_user():
#   print("Hello")

#   greet_user()






# while True:
#   try:
#     first_num = int(input("Enter your first num: "))
   
#     last_num = int(input("Enter your last num : "))
  

#     answer = first_num + last_num
#     print(answer)
#     con = input("do you want to continue y/n").lower()
#     if con == 'n':
#       break
#     else:
#       continue 
#   except ValueError:
#     pass
#   else:
#     print(answer)

import json

fi = [1,2,3,4,5,6,7,8]
filename = "ready.json"
with open('filename','w') as file:
    json.dump(fi,file)
  
with open('filename','r') as file:
    username = json.load(file)
    print(username)

  #Refactoring..

  