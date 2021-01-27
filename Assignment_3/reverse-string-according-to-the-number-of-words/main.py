inp='Ashish Yadav Abhishek Rajput Sunil Pundir Prem'
Out='merP linuS kehsihbA hsihsA Yadav Rajput Pundir'
lis= inp.split(' ')
new=[]
new2=[]
if len(lis)%2==0:
    
    for i in range(-1,-len(lis),-1):    
        
        if (i-1)%2==0:            
            new.append(lis[i][::-1])
    for i in range(0,len(lis)):
        if (i+1)%2!=0:
            new.append(lis[i])
else:
    
    for i in range(-1,-(len(lis)+1),-1):    
        
        if (i)%2!=0:            #odd
            new.append(lis[i][::-1])
    for i in range(0,len(lis)):
        if (i+1)%2==0:
            new.append(lis[i])    

print(' '.join(new))   
 