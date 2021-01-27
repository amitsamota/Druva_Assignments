'''
Tuple immutable
no assignment
indexing
slicing
tuple can be used as a key in dictionary ,,,, dictionary key is always immutable data type
tuple used when you don't want anyone to change elements
tup1 = ()
tup2 = 1,
tup3 = 1,2
tup4 = (1,2)
'''

t1 = (3,2,1)
t2 = (4,5,6)

print(t1+t2)    # concatenation

print(2*t1) #repetition

print(max(t1))
print(min(t1))

#print(t1.sort())  # no sorting

print(sorted(t1))  # sorted(tuple)

del t1 # deletes entire tuple


