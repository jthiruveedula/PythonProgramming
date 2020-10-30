# polymorphism:- ploy means--> many and morphism mean forms(same thing can perform many functions)
# method overloading:- It occurs when two or more methods in a class have same name having different params
# python didn't support method overloading directly but python do it in indirectly by using default arguments

# creating class
class methodOverLoadin:
    # creating method by assigning default arguments
    def __init__(self):
        pass

    def name(self, n=None):
        if (n == None):
            return ("not assigned anything")
        else:
            return n + " assigned !"


a1 = methodOverLoadin()
a2 = methodOverLoadin()
print(a1.name())
print(a2.name("Jagadeesh"))
