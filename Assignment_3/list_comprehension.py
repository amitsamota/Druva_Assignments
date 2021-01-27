odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)

odd.insert(4,13)  # insert at insert(index,element)

print(odd[4])

odd.append([15,17,19])          # append add element at the end of the list . it treats this as a single element
print(odd)

odd.extend([21,23,25])          # extends add element at the end of the list. it treats all elements as separate
print(odd)
#sort
#count
#index
#reverse

#print intersection or common of both list into one
l1=[1,2,3,4]
l2=[4,5,6,7]

l3 = [i for i in l1 if i in l2]
print(l3)

#print power of 2 of each element
'''pow2 = []
for x in l2:
   pow2.append(2 ** x)
   '''
l4 = [i**2 for i in l2]
l5 = [pow(i,2) for i in l2]
print(l4)
print(l5)

# Python code to convert list of
# string into sorted list of integer

# List initialization
list_string = [1, 12, 15, 21, 131]

# Using list comprehension
output = [str(x) for x in list_string]

# Printing output
print(output)