#Encapsulation is the process of protecting class attributes and methods from accidential modification and it does not allow to access the protected attributes or methods to outside.

#Attribute encapsulation

class encapsulation:

    def __init__(self) :
        self.a=10 #public access variable
        self._b=20 #private but can have internal access
        self.__c=30 #strictly restricted



a1 = encapsulation()
print(a1.a)
print(a1._b)
print(a1.__c) # strictly private we will get error
print(a1._encapsulation__c) # name mangling method to access restricted variables
