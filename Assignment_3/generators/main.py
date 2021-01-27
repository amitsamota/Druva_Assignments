'''
If a function contains at least one yield statement, it becomes a generator function. 
Both yield and return will return some value from a function.

return statement terminates a function entirely, yield statement pauses 
the function saving all its states and later continues from there on successive calls.

The major difference between a list comprehension and a generator expression is that a list comprehension
produces the entire list while the generator expression produces one item at a time.

They have lazy execution ( producing items only when asked for ).
For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.
'''


l=[1,2,3]


lco = [i*2 for i in l]
print(lco)

lgen = (i*2 for i in l)
print(lgen)
print(next(lgen))
print(next(lgen))