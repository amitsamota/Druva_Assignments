'''
Access modes:
    r : opens file for reading only
    rb : opens a file for reading only in binary format
    r+ : opens a file for both reading and writing
    w : opens a file only for writing
    wb : opens a file for write only in binary
    w+ : write and read mode ,   overwrites the existing file . create new file if not already created
    a : opens a file in append mode. pointer at the end of file.


'''

file = open('subject.txt', 'r')  # open(filename , access_mode , buffering)
print(file.read())  # reading the whole file
print(file.read(15))   #file.read([count]) count number of bytes or characters
file.close()  # closing the file , no more I/O on closed file
print('File is closed  : ', file.closed)  # return True if file is closed False otherwise
print('Name of file is :', file.name)  # returns name of file
print('Access mode of file :', file.mode)  # return access mode file



