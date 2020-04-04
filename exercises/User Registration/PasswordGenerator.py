import enum, random

class PasswordLevel(enum.Enum):
    WEAK = 0
    MEDIUM = 1
    STRONG = 2

class PasswordGenerator:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numericals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ['&', '*', '$', '#', '!']
    passChars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    def __init__(self, userAccount):
        self.userAccount = userAccount

    def generate(self, passwordLevel):
        passwordLevel = PasswordLevel(passwordLevel)
        if passwordLevel == PasswordLevel.WEAK:
            return self.generateWeakPassword()
        elif passwordLevel == PasswordLevel.MEDIUM:
            return self.generateMediumPassword()
        else:
            return self.generateStrongPassword()
        
    def generateWeakPassword(self):
        return self.userAccount.name + str(self.userAccount.mobile)
    
    def generateMediumPassword(self):
        password = list(self.userAccount.name)
        randomIndex = random.randint(0, len(self.userAccount.name)-1)
        password[randomIndex] = self.symbols[random.randint(0, len(self.symbols)-1)]
        randomIndex = random.randint(0, len(self.userAccount.name)-1)
        password[randomIndex] = str(self.numericals[random.randint(0, len(self.numericals)-1)])
        return "".join(password)

    def generateStrongPassword(self):
        return "".join(random.sample(self.passChars, random.randint(7, 13)))