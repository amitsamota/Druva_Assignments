'''
Method with same name but different number of arguments.
Last defined method will be called everytime.
So python directly don't support methodoverloading
'''


class A:

    def method_overload(self, arg1, arg2):
        print('in first')

    def method_overload(self, arg3, arg4, arg5):
        print('in second method')


a = A()
# a.method_overload(2, 3)                   # TypeError:method_overload() missing 1 required positional argument: 'arg5'
a.method_overload(2, 3, 4)

