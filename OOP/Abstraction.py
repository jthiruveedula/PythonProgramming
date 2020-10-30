#Abstraction:- Is the meachanisam of only declaring methods but not instantiated, declared methods are implemented in its child classes

from abc import ABC,abstractclassmethod

#initiating abstract and could be used in other child classes
class abstractClass(ABC):
    @abstractclassmethod
    def abstractMethod(self):
        pass

class childAbstractClass(abstractClass):

    def abstractMethod(self):
        return "Child Abstract triggered!"

class child2Abstract(abstractClass):
    def abstractMethod(self):
        return "Another child Abstract Triggered!"

# a= abstractClass() (Can't instantiate abstract class abstractClass with abstract methods abstractMethod)
# print(a.abstractMethod())
a1= childAbstractClass()
a2= child2Abstract()
print(a1.abstractMethod())
print(a2.abstractMethod())