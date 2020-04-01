import User, PasswordGenerator

class UserAccount(User.User):
    def __init__(self, name, age, mobile, email, userid):
        super().__init__(name, age, mobile, email)
        self.userid = userid
        self.passwordGenerator = PasswordGenerator.PasswordGenerator(self)

    def generatePassword(self, passwordLevel):
        self.password = self.passwordGenerator.generate(passwordLevel)

    def printUserInfo(self):
        print("User Details: \nName: ", self.name, "\nAge: ", self.age, "\nMobile: ", self.mobile, "\nEmail: ", self.email, "\nUserName: ", self.userid, "\nPassword: ", self.password)
