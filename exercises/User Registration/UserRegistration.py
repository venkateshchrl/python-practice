import UserAccount

name = input("Enter name: ")
age = int(input("Enter age: "))
mobile = int(input("Enter mobile: "))
email = input("Enter email: ")
userid = input("Enter username: ")
userAccount = UserAccount.UserAccount(name, age, mobile, email, userid)

passwordLevel = int(input("Choose level of Password Severity(0 - Weak, 1 - Medium, 2 - High): "))

userAccount.generatePassword(passwordLevel)

userAccount.printUserInfo()