print("Hello World!")

#even number using range 
i = list(range(2,13,2))
print(i)

square = []
for value in range(1,11):
    value = value**2
    square.append(value)
print(square)

#List comprehension
Squares = [values**2 for values in range(1,20,2)]
print(Squares)

#slicing a list 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])

#Looping through a slice 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())