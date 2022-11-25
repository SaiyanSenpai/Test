# json.load() takes a file object and returns the json object.
# It is used to read JSON encoded data from a file and convert
# it into a Python dictionary or list (depending on contents).

import json
#open the file to read from it

filename = 'data/employees.json'
#filename='data/employees_List.json'
with open(filename) as f:
    data = json.load(f) #read file data into Dict or list
print(type(data))
# looping through the json data
for i in data['employees']:
   print(i)

# Closing file
#f.close() #with open handles this
