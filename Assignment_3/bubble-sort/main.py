#Bubble sort
#With every new pass, the largest element in the list “bubbles up” to the end
#average- and worst-case complexity of O(n2).
import time

t=time.time()

l=[10,11,12,13,14]

n=len(l)  
#n=5
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]       

print(l)        
print(time.time()-t)
