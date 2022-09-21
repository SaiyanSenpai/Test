#Week 3 Practice Lists
print('---Lab Challenge 1---')

Courses = ["ET710","ET574","ENG310",]
print(Courses)
print(Courses[2])
print(Courses[0])

print('\n\n---Lab Challenge 2---')
del Courses[0]
del Courses[1]
Courses.insert(1,"ET575")
Courses.insert(2,"ET580")
Courses.insert(3,"ET585")
Courses.insert(4,"ET725")

print(Courses)
print(f'I am taking {len(Courses)} courses.')

print('\n\n---Lab Challenge 3---')
Courses.sort()
Courses.sort(reverse=True)
print(Courses)