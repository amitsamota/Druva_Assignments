'''
Method overriding is used when we want same or different functionality in subclass
'''
class Parent:

    def myMethod(self):
        print('Parent Class')


class Child(Parent):

    def myMethod(self):
        print('Child Class')


c = Child()
c.myMethod()



