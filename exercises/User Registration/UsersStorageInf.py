import enum

class StorageTypes(enum.Enum):
    DATABASE = 0
    FILE = 1

class UsersStorageInf:
    def __init__(self, storageType):
        self.storageType = StorageTypes(storageType)

    def initializeStorage(self, permissions):
        raise NotImplementedError("The method is not implemented")
    
    def closeStorage(self):
        raise NotImplementedError("The method is not implemented")

    def findUserByUserName(self, userName):
        raise NotImplementedError("The method is not implemented")

    def getUserList(self):
        raise NotImplementedError("The method is not implemented")

    def createUser(self, userAccount):
        raise NotImplementedError("The method is not implemented")

    def updateUser(self, userAccount):
        raise NotImplementedError("The method is not implemented")

    def deleteUser(self, userid):
        raise NotImplementedError("The method is not implemented")