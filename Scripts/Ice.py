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


class IceCreamStand (Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavor1):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = flavor1

    def display_flavor(self):
        print("The flavor are : ")
        for flav in self.flavor:
            print(flav.title())
flavor_list=['vanila','Butterscootch','strawberry']    
Ice = IceCreamStand('red dragon','Italian',flavor_list)
Ice.display_flavor()
Ice.describe_restaurant(number_served=5)
Ice.increment_number_served(served=10)