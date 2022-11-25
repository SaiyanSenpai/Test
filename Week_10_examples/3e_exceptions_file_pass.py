# to pass means to take no action, do nothing
# imagine we have to process 10,000 files
# And 1 is missing. Lets do the other 9,999 rather than crash.

# Set path and file variables.
#import sys

filename = 'someFile.txt'

# An exception with a 'silent' fail.
try:
    with open(filename) as file_object:
        data = file_object.read()
except FileNotFoundError:
    pass    # do not indicate that there was an error
    #sys.exit()        #force script to exit/stop running

print("go on to read the next file")
#the except clauses requires a statement
