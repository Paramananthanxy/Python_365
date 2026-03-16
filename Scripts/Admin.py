from user import Users

class Privileges():
    def __init__(self,privilege=['can add post','can delete post','can ban user']):
     self.privilege = privilege

    
    def show_privileges(self):
        print("The privilege of the admin....")
        for pri in self.privilege:
            print(f"\n {pri.title()}")

class Admin(Users):
    def __init__(self,first_name,last_name,login_attempts,**other_argument):
        super().__init__(first_name,last_name,login_attempts,**other_argument)
        self.Privilege = Privileges()
    