# Adding an else clause

n = 10
d = 0

# A try-except block with an else
try:
    x = n/d
except ZeroDivisionError:
    print("The demoninator cannot be 0!")
else:           # run this code once we know the 'try' code is safe
    print(x)

print("next statement...")
