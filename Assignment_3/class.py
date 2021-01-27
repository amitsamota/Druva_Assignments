'''
__init__ is a special method which is called class constructor or initialization method which is called when
you create a new instance(object) of a class.

By default first argument to each method is 'self'
'''


class A:
    def __init__(self):
        print('class constructor', end='  ')
        print('is called')

    def m(self):
        print('self passed automatically as first argument')


a = A()

setattr(a, 'x', 20)  # to Set attribute.if not exist then create
print(getattr(a, 'x'))  # To access the attribute of the object
print(hasattr(a, 'x'))  # Check if attribute exists or not . Returns True or False
delattr(a, 'x')  # Delete attribute of an object
print(hasattr(a, 'x'))  # Returns False as attribute is deleted
b = A()
a.m()

print(A.__doc__)  # Class documentation String or None if undefined
print(A.__name__)  # Class Nme
print(A.__dict__)  # Dictionary containing class namespace
print(A.__module__)  # Module name in which class is defined. This is __main__ in interactive mode
print(__name__)  # _Main_module name

print(isinstance(a, A))  # isinstance(obj, Class) returns true if obj is instance of class Class


class X:
    pass


class Y(X):
    pass


print(issubclass(Y, X))  # returns true if B is subclass of A   issubclass(sub,super)
