'''
MultiLevel Inheritance
Order of Execution Son --> Father  --> GrandFather
'''


class M:  # GrandFather


    def fn1(self):
        print("GrandFather Class")

    def fn2(self):
        print('GrandFather Function 2')


class N(M):  # Father

    def fn1(self):
        print("Father Class")


class P(N):  # Son

    def fn1(self):
        print("Son Class")


p = P()
p.fn1()
p.fn2()
'''
Multiple inheritance
class C is derived from class A and class B
order of execution depends on which class is given as first argument

'''


class A:  # Parent class
    def fun1(self):
        print('class A')


class B:  # Parent class
    def fun1(self):
        print('class B')


class C(B, A):  # Child class
    def fun2(self):
        print('class C')


c = C()
c.fun1()



