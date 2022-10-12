print('1.')
num = 10
div_by_3 = num%3
div_by_5 = num%5

if div_by_3 != 0:
    print(f'{num} is not divisible by 3')
else:
    print(f'{num} is divisible by 3')

if div_by_5 != 0:
    print(f'{num} is not divisible by 5')
else:
    print(f'{num} is divisible by 5\n')

print('2.')
num = 12

if num % 2 == 0:
    print(f'{num} is divisible by 2')
elif num % 4 == 0:
    print(f'{num} is divisible by 4')
else:
    print(f'{num} is not divisible by 2 or 4')
    
print("\n3. ")
num = 52

if (num % 2) == 0 and  num > 50:
    print(f'{num} is a positive even integer greater than 50')
elif (num % 2) != 0 and num<0:
    print(f'{num} is a negative odd integer')

    
print("\n4. ")
final_grade = 96


if final_grade >= 96 and final_grade <= 100:
    print(f"{final_grade} is a grade of A")

elif final_grade >= 64 and final_grade <=95:
    print(f"{final_grade} is a grade of Passing")
    
elif final_grade < 64:
    print(f"{final_grade} is a grade of Not passing")

