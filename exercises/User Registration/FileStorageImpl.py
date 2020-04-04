import UsersStorageInf
import os
from csv import DictReader

class FileStorageImpl(UsersStorageInf.UsersStorageInf):
    def __init__(self, storageType):
        super().__init__(storageType)

    def initializeStorage(self, permissions):
        if os.path.exists('users.csv') == False:
            self.fileObject = open("users.csv", "w+")
        else:
            self.fileObject = open("users.csv", permissions)
    
    def closeStorage(self):
        self.fileObject.close()

    def getUserList(self):
        csvReader = DictReader(self.fileObject)
        return list(csvReader)

    def createUser(self, userAccount):
        userAccountObject = userAccount.toDictObject()
        self.fileObject.seek(0)
        if self.fileObject.read() == '':
            for key in userAccountObject:
                self.fileObject.write(key + ",")
        self.fileObject.write("\n")
        for key in userAccountObject:
            self.fileObject.write(str(userAccountObject[key]) + ",")

    def updateUser(self, userAccount):
        raise NotImplementedError("The method is not implemented")

    def deleteUser(self, userid):
        raise NotImplementedError("The method is not implemented")