import platform

def greet(name):
    print "Hello, {0}!".format(name)
print "What's your name?"
name = raw_input()
greet(name)

for x in xrange(1, 5):
    print x

try:
    val = 10/a

except NameError, err:
    print err, 'Error Caused'

print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0



# the next() function is all that remains in Python 3 (calling the .next() method raises an AttributeError)
print 'Python', platform.python_version()


my_generator = (letter for letter in 'abcdefg')

print next(my_generator)
print my_generator.next()

'''
If you are on windows go to cmd and run below command :

python {path_to_python}\tools\scripts\2to3.py --output-dir={output_dir} -W -n {input_dir}
path_to_python = directory where Python is installed
output_dir = directory where to output the Python3 scripts
input_dir = directory from where to read the Python2 script

In My(AMIT SAMOTA) Case
python C:\Users\amit.samota\AppData\Local\Programs\Python\Python39\Tools\scripts\2to3.py --output-dir=
C:\Users\amit.samota\PycharmProjects\Assinment4\3.x -W -n C:\Users\amit.samota\PycharmProjects\Assinment4\main.py
'''

