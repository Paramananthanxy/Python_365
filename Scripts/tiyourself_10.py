import json
import unittest
filename = "C:/Python_Beg_to_Adv/Scripts/fav_num.json"
def making_file():   
        num = input("Enter the number :")
        
        with open(filename,'w') as f:
            json.dump(num,f)
        return num
def guess_num(unittest.TestCase):
    try:
        
        with open(filename,'r')as f:
            num = json.load(f)
            print(f"I know your favorite number it's {num}")
    except FileNotFoundError:
        fav = making_file()
        print(f"I know your fav number {fav}")
        

unittest.main()

guess_num()