'''
List is mutable
indexing
assignment
slicing
'''

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

l1.append(l2)  # appends the object
print(l1)

l3 = [1, 2, 3, 4]
l4 = [5, 6, 7, 8]

l3.extend(l4)  # appends the element of object
print(l3)

l5 = [10, 11, 12, 13]

print(l4 + l5)  # concatenate l5 to l4

print(2 * l5)  # repetition

del l5[1]  # delete exact element at index    del list(index)
print(l5)

l5.remove(10)  # remove item from list  list.remove(item)
print(l5)

print(max(l5))

print(min(l5))

print(l5.count(13))  # number of times 10 occurs in l5

print(l5.index(12))  # first index where 12 occured

l5.insert(3, 14)  # list.insert(index,element)
print(l5)

l5.reverse()  # reverses elements of list
print(l5)

l5.sort()  # sort in ascending order
print(l5)

l5.sort(reverse=True)  # sort in descending order
print(l5)

l5.pop(2)  # list.pop(index)

