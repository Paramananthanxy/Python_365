# python basics
# This basic is typically for me ... because i have some so called coding skills.. 
# so lets seee....

#Strings 

Note = "This is a string"

#String methods

print(note.upper())
print(note.lower())

#Adding Whitespace to strings with Tabs or Newlines
\t - tab space
\n - new line 

#Stripping Whitespace
Stripped used for removing the whitespace from the string
lstrip() for removing left side spaace
rstrip() for removiing right side space
strip() for removing the both side space
 

 #list
 bicycle = ["trek", "cannondale"]
 print(bicycle[0])

 we can print the exact value using index 

 #modifying the element in the list 
motorcycles = ['honda', 'yamaha', 'suzuki']
  print(motorcycles)
motorcycles[0] = 'ducati'
  print(motorcycles)

 #adding element in list 
 using append 

 motorcycles = ['honda', 'yamaha', 'suzuki']
 motorcycles.append('ducati')
 print(motorcycles)

 #inserting element in the list 

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'Ducati')
    print(motorcycles)

#removing element in the list 
using del statement 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

We can use pop() to remove the element from the list 
the pop is remove the last item of the list but in the stack its removing the first item in the analogy,

#removing an item by value

By using the remove() method.. if we didn't know the index or position of the value that time we can use 
the remove ()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
    print(motorcycles)
motorcycles.remove('ducati')
    print(motorcycles)

['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki'] 


#sorting a list by using sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)  # for reverse order 
print(cars)

['toyota', 'subaru', 'bmw', 'audi'] 

#Length
Finding the length of the list we can use length() method 
len(cars)
 4  --> output 


 4.Working with Lists 

 Looping through an Entire lsit

 magicians = ['alice', 'david', 'carolina']
 for magician in magicians:
 print(magician)

alice
david
carolina

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
 print("I can't wait to see your next trick, " + magician.title() + ".\n")

Alice, that was a great trick!
I can't wait to see your next trick, Alice.
David, that was a great trick!
I can't wait to see your next trick, David.
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

#indenting Unnecessarily

File "hello_world.py", line 2
     print(message)
     ^
IndentationError: unexpected indent 

This will make error in python because its unexpectedd indent


Making Numerical Lists:

using the range()
for i in range(1,10):
    print(i)

using range() to make a list of numbers:
number = list(range(1,6))
print(number)

even numbers:
i = list(range(2,13,2)) 
print(i)

Square number:
square = []
for value in range(1,11):
    value = value**2
    square.append(value)
print(square)

Simple Statics with a list of numbers:

>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45

#List Comprehensions:

A list comprehension allow us to generate this square list in single line.

Squares = [values**2 for values in range(1,20,2)]
print(squares)

#slicing a list :
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

looping through slice 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
u for player in players[:3]:
 print(player.title())

#copy list.

my_foods = ['pizza', 'falafel', 'carrot cake']
v friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


Tuples:
 Sometimes we will need to create a list that cannot be change. an immutable list is called a tuple.

 Writing over a Tuple
Although you can’t modify a tuple, you can assign a new value to a variable
that holds a tuple. So if we wanted to change our dimensions, we could
redefine the entire tuple:
u dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

v dimensions = (400, 100)
w print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
The block at u defines the original tuple and prints the initial dimensions. At v, we store a new tuple in the variable dimensions. We then print the
new dimensions at w. Python doesn’t raise any errors this time, because
overwriting a variable is valid:

Styling Your Code:
    Make your code as easy as possible to read.
    The style guide:
        PEP python Enhancement Propasal
    Line Length:
    1.Each line should be less than 80 characters PEP 8 also recommends that your limit all of your comments
      to 72 characters per line.
    Blank Lines:
        Blank line used between two section of the code and mostly helpfull for readability of our code.
Other Style Guidelines:
    4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/
        dev/peps/pep-0008/. You won’t use much of it now, but it might be interesting
        to skim through it
------------------------------------------------------------------------------------------------------------

#if statement:

Checking multiple conditions 
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >21
False
age_0 >= 21 or age_1 >= 21
False

Checking wheather a value is in a list:

 requested_toppings = ['mushrooms', 'onions', 'pineapple']
u >>> 'mushrooms' in requested_toppings
True
v >>> 'pepperoni' in requested_toppings
False

#Boolean Expressions:
game_active = True
can_edit = False 


#multiple elif blocks
if age < 4:
 price = 0
elif age < 18:
 price = 5
u elif age < 65:
 price = 10
v else:
 price = 5

 Checking for Special Items
 requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
u if requested_topping == 'green peppers':
 print("Sorry, we are out of green peppers right now.")
v else:
 print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

output:
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.
Finished making your pizza!
#dictionaries 

alien = {'color':'green'}
print(alien)

adding new key and value in the dictonary 
alien['x_position'] = 0
alien['y_position'] = 25

print(alien)

modifying values in a dicionary 

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

The alien is green.
The alien is now yellow.

Removing Key-value pairs 

for removing we use del method 

del alien['points']

#looping through dictionary's Keys in Order

using sort method in loop 

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(name.title() + ", thank you for taking the poll.")



 Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.


#####using set() method in for loop
set() remove the duplicates in the dictionary


#nesting in dictionary 

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
u aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)
 
 output:
 {'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}


#list in dictionary with nested loop 
av_lang = {
  'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
}

for name,language in fav_lang.items():
  print("\n The fav lang of ",name)
  for languages in language:
    print("\t",languages)

output:
Jen's favorite languages are:
 Python
 Ruby
Sarah's favorite languages are:
 C
Phil's favorite languages are:
 Python
 Haskell
Edward's favorite languages are:
 Ruby 

 #while loop using flags 

  active = True
v while active:
 message = input(prompt)

w if message == 'quit':
 active = False
x else:
 print(message)

 We can use the break statement to break the loop 


 #while loop using with list and dictionaries 
    Using while loops wiht list and dictionary allow you to collect store and organize lots of input to examine and report on later 

#Removing all instances of specific values from a list 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')

print(pets)


#Filling a dictionary with user input:

. We’ll store the data we
gather in a dictionary, because we want to connect each response with a
particular user:


###function

##Passing Arguments:
#positional Arguments
    The simplest way to
do this is based on the order of the arguments provided. Values matched
up this way are called positional arguments.


 def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

 describe_pet('hamster', 'harry')
 describe_pet('dog', 'willie') ------------> multiple function calling 

#order matters in positional arguments:
    def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')

Output:
I have a harry.
My harry's name is Hamster.


##Keyword arguments:
mentioning the key and passing the argument is better 
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

##default values:
def describe_pet(pet_name, animal_type='dog'):  ---> default value for animal_type parameter 'dog'



# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


##return value:
using return in function to return the function output 

When you call a function that returns a value, you need to provide a
variable where the return value can be stored. In this case, the returned
value is stored in the variable musician

 def get_formatted_name(first_name, last_name):
name.py """Return a full name, neatly formatted."""
v full_name = first_name + ' ' + last_name
w return full_name.title()
x musician = get_formatted_name('jimi', 'hendrix')
print(musician)

## A function can return any kind of words .. include more complicated data structure like list and dictionaries too..

## list passing only copy list_name[:] for passing the copy of the list not the original list 


#passing an Arbitrary Number of Arguments:

def make_pizza(*toppings):
 """Print the list of toppings that have been requested."""
 print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

* --> single star for arguments 
** --> double star's for keywords 


###import function and module 
we can create a function and we can call a function at any we want by using " IMPORT " module to we  can import a module

import car -->like that

car.car_man   ------>car module , car_man is a funciton

method 2 
from pizza import make_pizza  --> importing speciifc functions

method 3 
from pizza import make_pizza as mp 

mp(16,'subra') we can rename the function of make_pizza to mp()  simply so we can use it anyware 

from module_name import funciton_name as fn 

method 4

using as to give a module an alias 

import pizza as p 

p.make_pizza()       ---> renaming the module_name 

method 4:

from pizza import * ---> importing all the function from pizza 



## Styling Functions:
    1.Function should have descriptive names.
    2.These names should use lowercase.
    3.Descripitive names help you and others to understand.
    4.Every function should have a comment that explains concisely what the function does.
    5.Definition should be in docstring format.
    6.If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function
ends and the next one begins

##Classes:


## The Python Standard Library..
    The python standard library is a set of modules included with every python installation.



##Handling the error:

print(5/0)

#storing data 
---------------------
using json formate to store a data because its helpfull for read in every programming
language.by using json.dump() and json.load()


json.dump()  ---->used for store a data in a dump file 
json.load()  ---->used for load from the json file 

#Refactoring..
-----------------------
makeing the code easy and readable to dividing the code to more usable 

