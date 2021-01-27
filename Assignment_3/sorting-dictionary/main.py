from collections import OrderedDict as od

d={1:'f',5:'r',3:'a'}


x=sorted(d.items() , key=lambda item:(item[0]))    #sorting by key item[0]  , sotring by value item[1]
print(x)
