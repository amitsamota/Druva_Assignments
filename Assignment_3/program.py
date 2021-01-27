# Fibonacci series 0,1,1,2,3,5,8


n = 7
a = 0
b = 1

for i in range(n):
    print(a)
    b, a = a, a + b

# reverse without slice
s = 'right'
a = ''
for i in s:
    a = i + a
print(a)

# reverse without slice
j = ''
for k in range(4, -1, -1):
    j += s[k]
print(j)

d = {x: 6 for x in [0, 1, 2]}
print(d)

k = [i for i in [1, 2, 3] if i in [3, 4, 5]]
print(k)

t = (1, 2, 3, [5, 6, 7])

t[3][0] = 6
print(t)

# insertion sort  avg, wrst case O[n2]    best case o(n) list already sorted

l = [6, 3, 1, 2, 7]

for i in range(len(l)):
    for j in range(i + 1, len(l) - 1):
        if l[i] > l[j]:
            l[j], l[i] = l[i], l[j]
print(l)

# sorting dictionary on values
d = {1: 'a', 3: 'z', 2: 'c', 4: 'd'}

sorted_dict = sorted(d.items(), key=lambda whole_dict: whole_dict[1])  # sorting on value
print(sorted_dict)

'''
*
**
***
****
*****
'''

for i in range(1,6):
    print(i*'*')


'''
*****
****
***
**
*
'''
print('\n')
for i in range(5,0,-1):
    print(i*'*')

#armstrong number
n = 153
sum2=0
for i in range(len(str(n))):
    k = n % 10
    sum2 += pow(k, 3)
    n = n // 10

if n == sum2:
    print(sum2)


class A:

    @classmethod
    def class_method(cls,x,y,z):
        return A
    @staticmethod
    def static_method(r,s,t):
        return r
a = A()
ret = a.class_method(1,2,3)
print(ret)
stat_ret = a.static_method(5,6,7)
print(stat_ret)


a =[1,2,3]
b = a
a[2] = 4
print(b)
print(id(a))
print(id(b))
c = a.copy()
print(c)
a[2] = 3
print(c)
print(id(a))
print(id(b))
print(id(c))

import copy
s=[1,2]
k=copy.deepcopy(s)
j=copy.copy(s)
s[1] = 3
print(id(s))
print(id(k))
print(id(j))
print(s)
print(k)
print(j)
