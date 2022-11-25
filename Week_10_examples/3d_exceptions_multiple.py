# Handle Multiple possible exceptions

# Note that all of the following code does not produce traceback errors.
# A try-except block with an else
try:
    x = n/d
except NameError:   # error when variables do not have values
   print("Variables must have values!")
except ZeroDivisionError:
    print("The demoninator cannot be zero!")
else:           # run this code once we know the 'try' code is safe
    print(x)

n = 10
d = 0
try:       #test
    x = n/d
except NameError:    #handle
    print("Variables must have values!")
except ZeroDivisionError:  #handle
    print("The demoninator cannot be 0!")
else:           # run this code once we know the 'try' code is safe
    print(x)

n = 10
d = 5
try:
    x = n/d
except NameError:
    print("Variables must have values!")
except ZeroDivisionError:
    print("The demoninator cannot be 0!")
else:           # run this code once we know the 'try' code is safe
    print(x)


print("")
