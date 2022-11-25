# File not found is a common exception
#let's wrap the file read in a try block
import sys

# Set path and file variables.
#path = os.getcwd()
filename = 'someFile.txt'

# An exception used to check if a file exists.
try:
    with open(filename) as file_object:
        data = file_object.read()
except FileNotFoundError:
    print(filename+" does not exist")
    sys.exit()

print("Let's go on and read the next file if there is another")
print("or else we can choose to exit the program") #see exa 3a
