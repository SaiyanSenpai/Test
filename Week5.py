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
    
print("\n3.")
num = 52

if (num % 2) == 0 and  num > 50:
    print(f'{num} is a positive even integer greater than 50')
elif (num % 2) != 0 and num<0:
    print(f'{num} is a negative odd integer')

    
print("\n4.")
final_grade = 96


if final_grade >= 96 and final_grade <= 100:
    print(f"{final_grade} is a grade of A")

elif final_grade >= 64 and final_grade <=95:
    print(f"{final_grade} is a grade of Passing")

elif final_grade < 64:
    print(f"{final_grade} is a grade of Not passing")


print("\n5.")
grades = [95, 63, 80, 53, 90, 56]

passingGrades = [i for i in grades if i >=64]
passingGrades_Average = sum(passingGrades)/len(passingGrades)

total = 0
for grade in grades:
    if grade >= 64:
        total = total+grade
        passingGrades

print(passingGrades_Average)

print("\n6.")

numbers = [n for n in range(1,31)]
mult_of_3_and_5 = [n for n in numbers if n%3 == 0 or n%5 == 0]
mult_of_3_and_not_5 = [n for n in numbers if n%3 == 0 and n%5 != 0]
not_mult_of_3_and_5 = [n for n in numbers if n%3 == 0 and n%5 == 0]


print(numbers)
print(mult_of_3_and_5)
print(mult_of_3_and_not_5)
print(not_mult_of_3_and_5)