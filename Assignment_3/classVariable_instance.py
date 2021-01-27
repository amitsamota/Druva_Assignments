'''
Classs Variable and instance variable
Class variable defined outside of any method.
Instance variable belongs only to current instance of a class

'''


class A:
    x = 'class variable 1'  # class variable
    y = 'class variable 1'

    def __init__(self, ins1, ins2):
        self.x = ins1  # instance variable
        self.y = ins2


a = A('instance 1', 'instance 2')
print(a.x)  # it will print instance variable   OBJECT.VARIABLENAME
print(A.x)  # it will print class variable     CLASSNAME.VARIABLENAME
