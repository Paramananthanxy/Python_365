#OOPs 

#9.1 Restaurant && 9.4 Number served.

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.served = 0

    def describe_restaurant(self,number_served=0):
        print(f"\n The restaurant name is : {self.restaurant_name.title()}")
        print(f"The cuisine type is {self.cuisine_type.title()}")
        self.number_served = number_served
        print(f"Number of served: {self.number_served}")

    def open_restaurant(self):
        print(f"\n The {self.restaurant_name.title()} restaurant is open...!")

    def increment_number_served(self,served):
        self.served = served
        served_num = self.number_served + self.served
        print(f"The total number served today: {served_num}") 



r1 = Restaurant("A", "Italian",)
r1.describe_restaurant(43)
r1.increment_number_served(45)


print(r1.restaurant_name)

#9.2 Three Restaurants

r2 = Restaurant("Red Dragon","Chinese")
r2.describe_restaurant()
r3 = Restaurant("mossa",'russian')


#9.3 Users
class Users ():
    def __init__(self,first_name,last_name,login_attempts,**other_argument):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.login_attempts = 0
        self.other_argument = other_argument
        
        
    def describe_user(self):
        full_name = self.first_name+' '+self.last_name
        print(f"\n Your name: {full_name.title()}")
        for key,values in self.other_argument.items():
         print(f"{key.title()} is {values.title()}")

    def greet_user(self):
        full_name = self.first_name+' '+self.last_name
        print(f"\n Happy to have you {full_name.title()}")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"the login attempt is {self.login_attempts}")
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The login attempt is reseted : {self.login_attempts}")


    

    


    

