print("1)")
multiples = list(range(0,5*11,5))
count = 0
while count<11:
    print(multiples[count], end = " ")
    count = count+1
    
#another way
number = 0
while number<=50:
    print(number, end= " ")
    number+=5



print("\n2")
grades = []
while True:
    prompt = "Enter a grade or -1 to stop: "
    response = int(input(prompt))
    if response == -1:
        print(f'The GPA is {sum(grades)/len(grades):.0f}.')
        break
    else:
        grades.append(response)
#sentinel value is any value we put to break the loop
#in this case it's -1.
    

print("\n3")
grades = [96,34,67,88,90]
while min(grades) <=60:
     grades.remove(min(grades))
print(*grades,sep=" ")


print("\n4")
students = {}
number = 0
while number <3:
    number = number +1
    name = input("Enter name: ")
    grade_1 = input("Enter grade 1: ")
    grade_2 = input("Enter grade 2: ")
    grade_3 = input("Enter grade 3: ")
    students[name] = {"Grades" == {grade_1,grade_2,grade_3}}

print(students)
for student in students:
    for grade in student["Grades"]:
        print(*grade, sep=" ")
print("\n5")