"""
Understand Implicit and Explicit data type conversions. Write sample program and include at least 5 data type
conversion example.
"""

'''
In Implicit type conversion, Python automatically converts one data type to another data type. 
This process doesn't need any user involvement.
'''

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

'''
In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined
functions like int(), float(), str(), etc to perform explicit type conversion.
This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.
'''

num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))

# string variable
a = "5.9"

# typecast to float
n = float(a)

print(n)
print(type(n))

# int variable
a = 5

# typecast to str
n = str(a)

print(n)
print(type(n))


'''
Some more functions for explicit type casting:
    1.chr(number) – converts number to its corresponding ASCII character.
    2.int(str, base) – converts any data type to integer. base specifies the base in which string is if data type is string.
    The default value of base is 10, if it is not specified.
    
    3.float() – converts any data type to a floating point number.
    4.ord() – converts a character to integer.
    5.hex() – converts integer to hexadecimal string.
    6.oct() – converts integer to octal string.
    7.tuple() – converts the given data type to a tuple.
    8.set() – converts the given data type to a set.
    9.list() – converts the given data type to a list.
    10.dict() – converts the given ordered tuple to a dictionary.
    11.str() – converts the given data type to a string.
    12.complex(real,imag) – converts real numbers to complex(real, imag) number.
'''
