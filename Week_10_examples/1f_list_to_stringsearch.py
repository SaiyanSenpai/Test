# Searching data which you've read

# the csv is in the same folder as this py file

filename = 'deniro.csv'

# read file data into a list
with open(filename) as file_object:
    data_list = file_object.readlines()
print(data_list)

# create an empty string
# concatenate all file data into a single string without blank lines
text = ""
for line in data_list:
    text += line.rstrip()

# search a substring within a string
if "God" in text:
    print("Godfather found")
else:
    print("Godfather not found")

print("")

# Refresher about the 'in' keyword
# with strings, in checks for substrings
print("red" in "red")
print("red" in "reddington")
print("red" in "violet")
print('')
# how in checks for membership with lists/tuples
print("red" in ["blue", "red"])
print("red" in ["keen", "reddington"])
print('')
#In a dictionary, membership is seen as "being one of the keys":
print("samoyed" in {"samoyed": "ghost"})
print("samoyed" in {"ghost": "samoyed"})
