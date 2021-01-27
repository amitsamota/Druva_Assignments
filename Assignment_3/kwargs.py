

def fun(**kwargs):
    print(kwargs['Bucket'])
    print(kwargs['Creat_na']['LocationConstraint'])


buck_name = 'amit_bucket'

fun(Bucket=buck_name,
                          Creat_na={
                              'LocationConstraint': 'eu-west-1'})

