class Example:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @classmethod
    def class_method(cls,a,b):
        return cls(a,b+" ji")
    
    @staticmethod
    def static_method(a,b):
        return (a+" kumar")
        
exam= Example("Amit","Samota")
exam1 = Example.class_method("amit","samota")
print(exam1.last)
print(exam1.static_method(exam1.first,exam1.last))