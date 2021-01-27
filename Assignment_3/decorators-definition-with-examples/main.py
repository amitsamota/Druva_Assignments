'''
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object 
without modifying its structure.

Decorators have several use cases such as:
    1.Authorization in Python frameworks such as Flask and Django
    2.Logging
    3.Measuring execution time
    4.Synchronization

We can use multiple decorators to a single function.the decorators will be applied in the order that we've 
called them.Aplication of decorators is from the bottom up.

Always use functools.wraps when defining decorators. It will save you a lot of headache in debugging.    
'''

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return (splitted_string)

    return wrapper
    
def uppercase_decorator(decorated):
    def upper():
        return (decorated().upper())
    return upper
    
#Multiple decorators 
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())
