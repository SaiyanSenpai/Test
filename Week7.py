print("1)")
multiples = list(range(0,5*11,5))
count = 0
while count<11:
    print(multiples[count], end = " ")
    count = count+1
    
#another way
number = 0
while number<=50:
    print(number, end = " ")
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

    

print("\n3")

print("\n4")

print("\n5")