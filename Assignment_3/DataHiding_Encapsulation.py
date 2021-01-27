'''
Encapsulation hide data from outside world.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data
Private method or variable can be accessed only within the class
Private , Protected and Public are ACCESS specifiers.
dDclare variables as private or protected.
Private > two underscore    Protected > single underscore
If you want to change the value of a private variable, a setter method is used.  This is simply a method that sets the
value of a private variable.
'''


class Car:
    __maxspeed = 0
    __name = ""
    max = 4

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def settermethod(self, max):
        self.__maxspeed = max


redcar = Car()
redcar.drive()

redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()

redcar.settermethod(10)  # setter method will change value
redcar.drive()

'''
Instance variable names starting with two underscore characters cannot be accessed from outside of the class. 
At least not directly, but they can be accessed through private name mangling . We can access using #instance_name._classname__A.
'''


class A:
    __x = 3
    _y = 10


a = A()

print('Private variable accessed is : {}'.format(a._A__x))  # instance_name._classname__A.

print('Protected variable accessed is : {}'.format(a._y))
