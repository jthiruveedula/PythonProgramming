#polymorphism:- ploy means--> many and morphism mean forms(same thing can perform many functions)
#operator overloading:- one and the same operator is used to perform different operations
class operatorOverLoading:
    # create init method
    def __init__(self ,firstName ,lastName):
    # creating and initializing variables
        self.firstName = firstName
        self.lastName = lastName
    def __add__(self, other):
    # creating a method for string concat from other objects
        self.firstName = self.firstName + other.firstName
        self.lastName = self.lastName + other.lastName
        return operatorOverLoading(self.firstName, self.lastName)
    def __str__(self):
        #returning concat output from this class
        return  ("{},{}".format(self.firstName ,self.lastName))


#creating objects sand passing input
a1 =operatorOverLoading("Jaga" ,"Thir")
a2 =operatorOverLoading("deesh" ,"uveedula")
#adding two objects
print(a1 + a2)
