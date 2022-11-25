''' How to handle or catch exceptions-
Anticipate common error scenarios.
Add code that will replace Python's traceback reporting.
A try-except block.
'''
import sys
try:
    print(10/0)
# If the 'Try' block generates a ZeroDivisionError,
# run some warning code instead of producing a traceback error.
# This is known as 'catching' or 'handling' an 'exception'.
except ZeroDivisionError:
    print("The demoninator cannot be 0!")
    #sys.exit('Program exiting because..fill in the blank') # force the program to end
print("")
print("If we choose, our program continues executing on the next line")
print("and the one after that")
print("and the one after that")
print('unless we choose to end it...')
