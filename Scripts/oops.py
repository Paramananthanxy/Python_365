class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def roll(self):
        print(f"\n {self.name.title()}  can roll.. !")

dog1 = dog('ruby','13')
dog1.roll()


class Car():
    def __init__(self,name,model,milleage):
        self.name = name
        self.model = model


