from collections import OrderedDict
#Dictionary


#6.1 Person
order = OrderedDict()
order['First_name']='Allen',
order['Last_name']='swagger',
order['age']='22',
order['city']='New york'

for key,value in order.items():
    print(f"{key} : {value}")

#6.5 Rivers:

river = {
    'nile':'Egypt'
    ,'Ganga':'India'
    ,'Amazon':'Brazil'
}

for key,value in river.items():
    print("The ",key," runs through ",value)


#6.7 Peoples
person ={ 'allen':{
    'First_name':'Allen',
    'Last_name':'swagger',
    'age':'22',
    'city':'New york'
},
    'rudy':{
         'First_name':'rudy',
    'Last_name':'swagger',
    'age':'22',
    'city':'New york'
    }

}

for user,user_info in person.items():
    print("\n The user is ",user)
    full_name = user_info['First_name'] + " " + user_info['Last_name']
    age = user_info['age']
    city = user_info['city']

    print("Full name : "+full_name)
    print("Age : ",age)
    print("Location",city)

#6.8 Pets:

    dog = {
        'name':'julie',
        'owner':'riya'

    }
    cat = {
        'name':'ruby',
        'owner':'rose '

    }

    pets = [dog,cat]
    for pet in pets:
        print(pet)

#6.9 Favorite places:
    fav_place = {
        'allen':['thailand','bankok','russia'],
        'rose':['swize','England','paris'],
        'ageon':['queensland','north','castleblack']
    }

    for name,nam_info in fav_place.items():
        print("\n Fav place for ",name)
        for nam_info in nam_info:
            print(nam_info)


#6.11 Cities && 5.12 Extensions
cities = {
    'paris':{
        'country':'france',
        'population':'10M'
    },
     'delhi':{
        'country':'india',
        'population':'14M'
    },
     'Newyork':{
        'country':'USA',
        'population':'15M'
    }
}

for city,city_info in cities.items():
    print("\n the name of the city: ",city)
    country = city_info['country']
    population = city_info['population']
    print("Country : ",country.title())
    print("Population : ",population.title())