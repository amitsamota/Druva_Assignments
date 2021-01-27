'''Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared,but contains
 no implementation.Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
'''

from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    def __init__(self):
        print('hi')

    @abstractmethod
    def do_something(self):
        print('Main Abstract Class')


class AnotherSubClass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print('Sub Class of Abstract Example')


obj1 = AnotherSubClass()
obj1.do_something()

'''

class Abstract():

    def so_something(self):
        print('main class')

class Another(Abstract):

    def so_something(self):
        super().so_something()
        print('sub class')
ob = Another()
ob.so_something()
'''
