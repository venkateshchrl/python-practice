import UserAccount , DBStorageImpl

class UserManagementSystem:
    def __init__(self):
        self.storageHandler = DBStorageImpl.DBStorageImpl(0)

    def displayAvailableOptions(self):
        print("1. Add New User")
        print("2. Update User")
        print("3. Get Users List")
        print("4. Find User")
        print("5. Delete User")
        print("6. Exit")

    def addUser(self):
        name = input("Enter Name: ")
        try:
            age = int(input("Enter Age: "))
        except ValueError as ve:
            raise ve             
        mobile = int(input("Enter Mobile: "))
        email = input("Enter Email: ")
        userid = input("Enter Username: ")
        userAccount = UserAccount.UserAccount(name, age, mobile, email, userid)
        passwordLevel = int(input("Choose level of Password Severity(0 - Weak, 1 - Medium, 2 - High): "))
        userAccount.generatePassword(passwordLevel)
        self.storageHandler.initializeStorage("a+")
        self.storageHandler.createUser(userAccount)
        self.storageHandler.closeStorage()
        print("User added successfully")
        return userAccount

    def updateUser(self):
        userid = input("Enter Username of the user to be updated: ")
        self.storageHandler.initializeStorage("a")
        userAccount = self.storageHandler.findUserByUserName(userid)
        if(userAccount != None):
            print("User Details: ", userAccount)
            name = input("Enter Name["+ userAccount["name"] + "]: ")
            if name == '':
                name = userAccount["name"]
            age = input("Enter Age["+ str(userAccount["age"]) + "]: ")
            if age == '':
                age = str(userAccount["age"])
            mobile = input("Enter Mobile["+ str(userAccount["mobile"]) + "]: ")
            if mobile == '':
                mobile = str(userAccount["mobile"])
            email = input("Enter Email["+ userAccount["email"] + "]: ")
            if email == '':
                email = userAccount["email"]
            userAccount = UserAccount.UserAccount(name, age, mobile, email, userid)
            passwordLevel = int(input("Choose level of Password Severity(0 - Weak, 1 - Medium, 2 - High): "))
            userAccount.generatePassword(passwordLevel)
            self.storageHandler.updateUser(userAccount)
            print("User updated successfully")
        else:
            print("No User found with specified user id")
        self.storageHandler.closeStorage()

    def getUsersList(self):
        self.storageHandler.initializeStorage("r")
        print(self.storageHandler.getUserList())
        self.storageHandler.closeStorage()

    def findUserByUserName(self):
        userid = input("Enter Username of the user to be found: ")
        self.storageHandler.initializeStorage("r")
        print(self.storageHandler.findUserByUserName(userid))
        self.storageHandler.closeStorage()

    def deleteUser(self):
        userid = input("Enter Username of the user to be deleted: ")
        self.storageHandler.initializeStorage("d")
        self.storageHandler.deleteUser(userid)
        print("User deleted successfully")
        self.storageHandler.closeStorage()

    def chooseOperation(self, optionChosen):
        if optionChosen == 1:
            self.addUser()
        elif optionChosen == 2:
            self.updateUser()
        elif optionChosen == 3:
            self.getUsersList()
        elif optionChosen == 4:
            self.findUserByUserName()
        elif optionChosen == 5:
            self.deleteUser()
        else:
            exit()
        self.displayAvailableOptions()
        self.chooseOperation(int(input("Choose a option: ")))

def main():
    ums = UserManagementSystem()
    print("Welcome to User Management System:")
    ums.displayAvailableOptions()
    ums.chooseOperation(int(input("Choose a option: ")))
#main()