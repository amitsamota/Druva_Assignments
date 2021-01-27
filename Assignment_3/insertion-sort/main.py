#Insertion sort
#With every new pass, the samllest element in the list “inserted” in the front
#average- and worst-case complexity of O(n2).
import time

t=time.time()

l=[8,7,5,6,1]

n=len(l)  

for i in range(n):
    for j in range(i+1,n):
        
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]   
            
print(l)
print(time.time()-t)

