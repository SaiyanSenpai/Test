# To extract a string that contains all characters in the file
# use file.read()

# set path and file variables
filename = 'data/states.txt'

# file contents are available via the 'file_object'
# f = open(filename, mode)    mode defaults to read
# the  open function returns a file object

with open(filename) as file_object:
    data = file_object.read()

print(data)
print(type(data)) #data is a string
