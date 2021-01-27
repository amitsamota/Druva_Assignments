from functools import *


def fun(l):
    for i in l:
        yield i


l = [1, 2, 3, 4]
for i in fun(l):
    print(i)

l = [1, 2, 3, 4, 5, 6]
filtered_list = list(filter(lambda x: x % 2 == 0, l))
print(filtered_list)

mapped_list = list(map(lambda x: x * x, l))
print(mapped_list)

reduced = reduce(lambda x, y: x + y, l)
print(reduced)

i = 5
while (i > 0):
    print('value of i {}'.format(i))
    i -= 1

z1 = [1, 2, 3]
z2 = ['one', 'two', 'three', 'four']
zipped_list = list(zip(z1, z2))
print(zipped_list)

import re

st = 'holidayho'
pat = 'ho'
x = re.search(pat, st)
y = re.findall(pat, st)  # returns all the pattern where matched

print(x.span())
print(y)


