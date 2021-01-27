def doublestarargs(**args):
    print (list(args.items()))

#ar1 = {'name' :'Amit','surname':'Samota'}                #we can't pass this as argument to **args as this will throw error
doublestarargs(name = 'Amit' , surname = 'Samota')       # arguments should be in this form