# When you see write, think overwrite.
# Review contents of data_3.txt before running this

# set path and file variables
filename = 'data/data_3.txt'

# open and write to a file (overwrite existing file data)
with open(filename, 'w') as file_object:
    file_object.write('Extra Fresh Data has been written to '+filename+'\n')

# open and read from the file (that you just wrote to)
with open(filename) as file_object:
    print(file_object.read())

print("")

# https://www.w3schools.com/python/python_file_write.asp
