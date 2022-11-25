# Convert from list to string

# set path and file variables
filename = 'data/data_1.txt'

# read file data into a list
with open(filename) as file_object:
    data = file_object.readlines()
print(data)
print(type(data))
# create an empty string
# concatenate all file data into a single string without blank lines
text = ""
for line in data:
    text += line.rstrip()

# print the string
print(text)
print(type(text))
print("")
