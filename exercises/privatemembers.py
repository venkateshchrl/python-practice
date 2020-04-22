# Python program to  
# demonstrate private members 
  
# Creating a Base class 
class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self._c = "GeeksforGeeksProtected"
        self.__d = "GeeksforGeeksPrivate"

    @staticmethod
    def addNum(num1, num2): 
        return num1 + num2

    def getCValue(self):
        return self._c
    
    def getDValue(self):
        return self.__d
    
    def printUserDetails():
        print("User Details: Name: Venkatesh")

    def print(self):
        print("Print from Base")

# Creating a Base class 
class Base1: 
    def print(self):
        print("Print from Base 1")

# Creating a derived class 
class Derived(Base1, Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base1.__init__(self)
        Base.__init__(self)  
        print("Calling protected member of base class: ") 
        print(self._c) 

        print("Calling private member of base class: ") 
        print(self.getDValue()) 

    
# Driver code 
print("==========================================")
obj1 = Derived() 
setattr(obj1, "a", "GeeksforGeeksPublic")
print(obj1.a)
print("==========================================")
print(dir(obj1))
print("==========================================")
print(obj1._Base__d)
print("==========================================")
print(Derived.addNum(2,5))
print(Base.printUserDetails())
print(obj1.print())