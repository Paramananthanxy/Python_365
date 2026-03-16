###passing information in a funciton..
def greet(name):
    print(name," How are you!")
greet('jessy')

def describe_pet(type1,name):
    print(f"\n I have a {type1.title()}")
    print(f"Its name is : {name.title()}")

describe_pet('Hamster','hendry')
describe_pet('dog','rose') #--------------> multiple funciton calls 

##Default value 


def describe_pet(type1,name = 'radio'):
    print(f"\n I have a {type1.title()}")
    print(f"Its name is : {name.title()}")

describe_pet('Hamster','hendry')
describe_pet('dog','rose')
describe_pet('cat')  ##default value 
describe_pet(type1='hamster', name='harry') ##keyword argument


##return function

#Returing a dictionary.

def simple(fname,lname):
    funame = {'first':fname , 'last':lname}
    return funame
name =  simple('randy','Orton')
print(name)


def persons(fname,lname,age=' ' ):
    funame = {'first':fname,'last':lname}
    if age:
        funame['age']=age
    return funame
person = persons("jimi",'redy','27')
print(person)

#using function with while loop

# def name(fname,lname):
#     formate = fname +' '+lname
#     return "hello mister/miss"+' '+formate.title()

# pool = True
# while pool:
#     f_name = input("\n Enter the First name : ")
   
#     if f_name.lower() =='no':
#         break
#     l_name = input("\n Enter the Last name : ")
#     muscian = name(f_name,l_name)
#     print(muscian)

#Passing list in function


def user(name):
    for msg in name:
        print(f"Hello {msg} !")
    
name = ['hannah', 'ty', 'margot']
user(name)
    
#models

def model(unprinted_designs,completed_models):
    while unprinted_designs:
        created_design = unprinted_designs.pop()
        completed_models.append(created_design)
        # print(completed_models)
    
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
      print(completed_models)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

model(unprinted_designs,completed_models)
# print(unprinted_designs,completed_models)
show_completed_models(completed_models)

