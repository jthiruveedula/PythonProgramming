#Encapsulation is the process of protecting class attributes and methods from accidential modification and it does not allow to access the protected attributes or methods to outside.

#Method Encapsulation

class methodEncapsulation:

    def public(self):
        return "I'm public method and can be accessed by anyone!"

    def _private(self):
        return "Hey I'm private method and can only be accessed internally!"
    def __strictlyPrivate(self):
        return  "Hey I'm strictly restricted so you can't access me!"

class dummy(methodEncapsulation):
    def __init__(self):
        pass


a1 = methodEncapsulation()

print(a1.public())
print(a1._private())

# print(a1.__strictlyPrivate()) # AttributeError

print(a1._methodEncapsulation__strictlyPrivate()) #using name mangling technique we can access this method

#we can access all method by inheriting
a2 = dummy()

print(a2.public())
print(a2._private())
print(a2._methodEncapsulation__strictlyPrivate())