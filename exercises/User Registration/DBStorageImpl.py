import UsersStorageInf, pymongo

class DBStorageImpl(UsersStorageInf.UsersStorageInf):
    def __init__(self, storageType):
        super().__init__(storageType)

    def initializeStorage(self, permissions):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client["usermanagementsystem"]
        self.collection = self.database["users"]
    
    def closeStorage(self):
        pass

    def getUserList(self):
        return list(self.collection.find({}, { "_id": 0}))

    def createUser(self, userAccount):
        userAccountObject = userAccount.toDictObject()
        self.collection.insert_one(userAccountObject)

    def findUserByUserName(self, userName):
        query = {"userid": userName}
        return self.collection.find_one(query)

    def updateUser(self, userAccount):
        query = {"userid": userAccount.userid}
        userAccountObject = {"$set": userAccount.toDictObject()}
        self.collection.update_one(query, userAccountObject)

    def deleteUser(self, userid):
        query = {"userid": userid}
        self.collection.delete_one(query)