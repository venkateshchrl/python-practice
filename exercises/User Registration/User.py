class User:
    def __init__(self, name, age, mobile, email):
        self.name = name
        self.age = age
        self.mobile = mobile
        self.email = email

    def printUserInfo(self):
        print("User Details: \nName: ", self.name, "\nAge: ", self.age, "\nMobile: ", self.mobile, "\nEmail: ", self.email)