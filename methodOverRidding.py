# Method Overridding occurs when there are two methods with the same method name and parameters, One of the methods is in parent class and other in child class.


class sampleA:

    def __init__(self):
        pass

    def same(self):
        return "I'm from SampleA:- parent method"
class sampleB(sampleA):
    def __init__(self):
        pass

    def same(self):
        return "I'm overridding sampleA:- Child SampleB"


a1=sampleA()
a2=sampleB()
print(a1.same())
print(a2.same())