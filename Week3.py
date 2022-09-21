#Week 3 Practice Lists
print('---Lab Challenge 1---')

courses = ["ET710","ET574","ENG310",]
print(courses)
print(courses[2])
print(courses[0])

print('\n\n---Lab Challenge 2---')
del courses[0]
del courses[1]
courses.insert(1,"ET575")
courses.insert(2,"ET580")
courses.insert(3,"ET585")
courses.insert(4,"ET725")

print(courses)
print(f'I am taking {len(courses)} courses.')

print('\n\n---Lab Challenge 3---')
courses.sort(reverse=True)
print(courses)

print('\n\n---Lab Challenge 4---')
numbers = []
numbers.append(2)
numbers.append(4)
print(numbers)

numbers.insert(0,0)
numbers.insert(1,1)
numbers.insert(2,2)
numbers.insert(3,3)
numbers.insert(4,4)
print(numbers)

save = numbers[2]
numbers.remove(2)
print(save)
print(numbers)

numbers.append(5)
print(numbers)



print('\n\n---Lab Challenge 5---')
print()