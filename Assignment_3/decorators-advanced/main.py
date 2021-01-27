import functools

usr_name=str(input(''))    #any string name
acc_lev =int(input())    #can be 0=admin,1=user,2=guest
user={'username':usr_name,'access_level':acc_lev}
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args,**kwargs):
        if user['access_level'] == 0:
            return func(*args,**kwargs)
        else:
            return 'no user permission for user {}'.format(user['username'])
        
    return secure_function

@make_secure()
def get_admin_password():
    return "admin : 1234"

@make_secure()
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())