#Another way to populate a list from a file

filename = 'data/states.csv'

data = []  # an empty list

# strip trailing lines as you store the data into a list
with open(filename) as file_object:
    for line in file_object:    #loop thru the file object
        data.append(line.rstrip())

# print the stripped list
for d in data:
    print(d)

print('')
print(type(data))
