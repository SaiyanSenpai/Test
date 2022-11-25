# append maintains existing file data and appends to it
# set path and file variables
filename = 'data_3.txt'   # note - not the data folder

# open and append to a file (add data, does not overwrite)
with open(filename, 'a') as file_object:
    file_object.write('Even More data has been written to '+filename+'\n')

# open and read from the file (that you just wrote to)
with open(filename) as file_object:
    print(file_object.read())

print("")
