#8.1 Message


def display_message():
    print("Hey i am learning funciton in python crash coursebook")
display_message()

##8.2 Favorite Book 
def favorite_book(title):
    print(f"My favorite book is {title.title()} ")

favorite_book('alice in wonderland')


#8.3 T-Shirt && 8.4 Large shirt default

def make_Shirt(size="l",text="I love python"):
    print(f"Size of the T-shirt is  {size.upper()}")
    print(f"The message you want is .. {text.title()}")

make_Shirt("m","Devil born")
make_Shirt(text = 'They dont care about us....! ',size = 'l')

##8.5 Cities:
def describe_city(city,country="India"):
    print(f"{city.title()} is in {country.title()}")

describe_city("chennai","India")
describe_city("moscow")

#8.6 City Names:
def city_country(city,country):
    return ' " '+ city.title()+', '+ country.title()
place = city_country('santiago','chile')
print(place)

#8.7 Album

def make_album(artist_name,title,index=None):
    album = {'artist':artist_name,'title':title}
    if index is not None:
        album['index']=index
    return album

album = make_album('anirudh','Yennakkena yarum illayae','1')
print(album)
album = make_album(title = 'smack that',artist_name='eminem')
print(album)

#8.8 useralbum

# def make_album(artist_name,title,index=None):
#     album = {'artist':artist_name,'title':title,}
#     if index is not None:
#         album['index']=index
#     return album
# Pool = True
# while Pool:
#     artist = input("\n Enter the artist name : ")
#     title = input("Enter the title of the song : ")
#     index = input("Enter the index number :")
#     if index =="":
#         index = None
#     album = make_album(artist,title,index)
#     print(album)
#     quit = input("if you want to continue type yes/no " )
#     if quit.lower() == 'no':
#         Pool = False
#         print("Thanks for your response ")
#         break
         
#     else:
#         continue

#8.9 Magicians && 8.10:

magicians = ['rambo','randy','rudy','batman']

def magic(magician):
    for mag in magician:
        print(f"The magician name is {mag.title()}")


magic(magicians)
#8.10 great magicians && 8.11 unchanged magicians: 
magicians = ['rambo','randy','rudy','batman','bruno']
great_magicians = []
def magics(magicians,great_magicians):
    while magicians:
        mag = magicians.pop(0)
        if mag.startswith("b"):
            great_magicians.append(mag)

def great_mag(great_magicians):
    for mag in great_magicians:
        print(f"The great magicians are : {mag}")


magics(magicians[:],great_magicians)
great_mag(great_magicians)
        

##Passing an Arbitrary number of Arguments :

#8.12 Sandwiches:
def sandwich(*sandwich_toppings):
    print("\n The sandwich topping you wanted is : ")
    for sand in sandwich_toppings:
       
        print(f"{sand.title()}")
sandwich('pepper','chicken','egg','rosemarry')

#8.13 user profile:

def user_profile(first_name,**other_details):
    person = {} 
  
    for key,value in other_details.items():
        person[key]=value

    return person

 
mag1 = user_profile('albert', last_name='einstein',location='princeton',)
print(mag1)

#8.14 Cars:
def car_man(car_name,manfacturer,**other_details):
    cars = {}
    cars[car_name]=car_name
    cars[manfacturer]=manfacturer
    for key,value in other_details.items():
        cars[key]=value
    return cars
car = car_man('subaru', 'outback', color='blue', tow_package=True)
print(car)






    
