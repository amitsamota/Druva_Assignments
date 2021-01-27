'''
Python deletes unneeded class instances automatically to free memory space and this is called Garbage Collection.
Garbage Collector runs during program execution and is triggered When an object reference counts eaches zeo
'''


class A:
    print('Class A')


class B:
    print('class B')


a = A()
b = a
c = a
d = b

print(id(a))
print(id(b))
print(id(c))
print(id(d))
