'''
The print_msg() function was called with the string "Hello" and the returned function was bound to the name another. On calling another(), the message was still remembered although we had already finished executing the print_msg() function.

This technique by which some data ("Hello") gets attached to the code is called closure in Python.

This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.
'''
def print_msg(msg):
    #This is outer enclosing function
    def nested():
    #This is nested function    
        print(msg)
    return nested

another=print_msg('Hello')
another()
del print_msg
another()