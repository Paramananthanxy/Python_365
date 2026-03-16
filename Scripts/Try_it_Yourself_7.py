#7.4 Pizza toppings 


# prompt = "\n Enter the pizza topping. What you want"
# prompt += "\n If you are done type 'quit'  "

# message =""
# while message != 'quit':
#     message =input(prompt)
#     print(message)
#     if message == 'quit':
#         print(message )

#7.5 Movie Tickets:
# prompt = "Enter your age for movie ticket :"

# in this program we using boolean while True for the program
# while True:
#     age = input(prompt)

#     if age =='quit':
#         break
#     age = int(age)
#     if age < 3:
#         print("The ticket is free ")
#     elif age <= 12:
#         print("The ticket price is $10")
#     elif age > 12:
#         print("The ticket price is $15")

#7.7 Infinity

# a =1 
# while a < 5:
#     print(a)

#7.8 Deli

sandwich_orders = ['suda','jammie','rose','rainbow']
finished_sandwich = []
while  sandwich_orders:
    sand = sandwich_orders.pop()
    print(f"I made your {sand}")
    finished_sandwich.append(sand)
print("The completed sandwiches are")
for finish in finished_sandwich:
    print(finish)

#7.9 No pastrami from 7.8 
sandwich_orders = ['suda','jammie','pastrami','pastrami','rose','pastrami','rainbow','pastrami']
finished_orders =[]
print("Deli has run out of pastrami")
while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')
    sand = sandwich_orders.pop(0)  ##important i used pop(0) for defining the index for removing 
    # if sand == 'pastrami':
    #     sand.pop('pastrami')
    finished_orders.append(sand)
print("The completed sandwiches are :")        
for finish in finished_orders:
    print(finish)

#7.10 Dream Vacation:

peoples = {}
poll = True
while poll :
    name = input("Enter your name:")
    place = input("If you could visit one place in the world,Where would you go? ")
    peoples[name]=place
    response = input("Do you want to continue this poll type 'yes' or'no'" ).lower()
    if response == 'no':
        poll = False
        break
    elif response =='yes':
        break
    else :
        print("Please type yes or no.")
        print("\n -----------Pooling completed-----------------")
for name,place in peoples.items():
    print(f"{name.title()} his dream place is {place.title()}")

#
