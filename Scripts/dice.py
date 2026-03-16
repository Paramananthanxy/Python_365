from random import randint

class Dice():
    def __init__(self,sides=6):
        self.sides = sides
        
    
    def roll_die(self):
        self.sides = randint(1,20)
        print(f"Your dice number : {self.sides}")


di = Dice()
di.roll_die()
