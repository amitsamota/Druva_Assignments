'''
Key and value pair  {key : value}
Key always of immutable data type like int , string , tuple
Values can be of any type
No duplicate key is allowed.When duplicate keys are encountered last key wins
d= {}
'''

d = {1:'One',2:'Two',3:'Three',3:'Three Last Value'}

print(d[1])     # accessing value

d[1] = 'One Updated'  # updation of value

print(d[1])

print(d[3])

print(str(d))   #string representation of dictionary


print(d.copy()) # returns shallow copy of dictionary
print(id(d))
print(id(d.copy()))

l = [7,8,9]
y=d.fromkeys(l,'default')   #dictionary.fromkeys(sequence , value)
print(y)

d.get(1)

print('dictionary keys \t{} '.format(d.keys()))
print('dictionary values \t{} '.format(d.values()))
print('dictionary items \t{} '.format(d.items()))
d2={4:'New Four'}

d.update(d2)    # update dictionary add d2  to d
print(d)

d.clear()   # removes all element of a dictionary

'''
del d   # deleted entire dictionary

d1 = {['list_key']: 'Mutable key not allowed'}

print(['list_key'])  # error unhashable type list
'''