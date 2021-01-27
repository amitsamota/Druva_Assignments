'''
if we use + operator it will throw error .
so we used inbuilt __add__ method to add two vector nad this is called operator overloading
'''

class Vector:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def __str__(self):
        return 'Vectors are ({},{})'.format(self.var1, self.var2)

    def __add__(self, other):
        return Vector(self.var1 + other.var1, self.var2 + other.var2)


obj1 = Vector(1, 2)
obj2 = Vector(4, 5)

print(obj1+obj2)
