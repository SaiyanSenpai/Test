from telnetlib import theNULL


num = 10
div_by_3 = num%5

if div_by_3 != 0:
    print(f'{num} is not divisible by 3')