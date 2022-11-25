'''
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.
'''
strng = "ny_economy, financial, business services, healthcare"
# split the string by spaces and store each segment into a list.
data = strng.split(',') #split returns a list
#data =strng.split() #note the commas are not removed
print(type(data))
print(data)
