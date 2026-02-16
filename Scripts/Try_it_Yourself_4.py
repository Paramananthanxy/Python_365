pizza = ['Pizza','Pitza','peessaa']
for pizzas in pizza:
    print("I love this ",pizzas)
print("\n This are my favouirate pizza's")
print("Because this pizzas or so yammiiii.....")

#4.3 Counting to Twenty:

count = [ value for value in range(1,21)]
print(count)

#4.4 one million
# mill =[value for value in range(1,1000001)]
# print(mill) 

# #4.5 summing a million
# print(min(mill),max(mill))
# print("\n", sum(mill))

#4.6 Odd numbers:
odd = [value for value in range(1,21,2)]
print(odd)

#4.7 Threes 
three = [value*3 for value in range(3,31)]
print(three)

#4.8 Cubes && 4.9 cube comprehension
cubes = [values**3 for values in range(1,11)]
print(cubes)

#4.10 slices

print("First three numbers",cubes[:3])
print("\n Middle of the list",cubes[5:8])
print("\n Last three numbers: ", cubes[7:11])

#4.11 My Pizza, Your Pizzas:

my_pizza = ['Pizza','Pitza','peessaa']
my_fri = my_pizza
my_pizza.append('mackronipizza')
my_fri.append('marshmello')
for pizzas in my_pizza:
    print("I love this ",pizzas,)
print("\n This are my favouirate pizza's")
print("Because this pizzas or so yammiiii.....")


#4.13 Buffet


Buffet = ('Briyani','Chicken','rice','chappathi','Idly')
for food in Buffet:
    print("The available foods :",food)

Buffet = ('Briyani','Chicken','rice','cPoori','Dosa')
for food in Buffet:
    print("The available foods :",food)