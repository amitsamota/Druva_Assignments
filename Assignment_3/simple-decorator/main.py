def func2(argum):
    
    def inter():
        print('internal before')
        
        argum()
        
        print('internal after')
    return inter 

@func2
def func1():
   print('function 1') 
    
#func1=func2(func1)    
func1()