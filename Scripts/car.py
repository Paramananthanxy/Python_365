class Car():
    def __init__(self,name,model,milleage):
        self.name = name
        self.model = model
        self.milleage = milleage

    def describe_car(self):
        print(f"The car is{self.name} the model is {self.model} millage is {self.milleage}")

class battery():
    def __init__(self,capacity=75):
        self.capacity = capacity

    def show_battery(self):
        print(f"The battery percentage is {self.capacity}")
    
    def get_range(self):
        car_range = self.capacity * 2 
        print(f"the car range {car_range} km")


    def upgrade_battery(self):
        self.capacity +=10
        print("battery upgraded")
        self.get_range() 

        print(f"The battery percentage is increased by {self.capacity}")
class Electriccar(Car):
    def __init__(self,name,model,milleage):
        super().__init__(name,model,milleage)
        self.battery = battery()


e1 = Electriccar('Tesla','s2','240')
e1.battery.show_battery()
e1.battery.upgrade_battery()
e1.battery.upgrade_battery()
e1.battery.upgrade_battery()

    