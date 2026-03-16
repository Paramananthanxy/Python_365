class Users ():
    def __init__(self,first_name,last_name,login_attempts=0,**other_argument):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
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





