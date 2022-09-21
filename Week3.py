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


letters = ['a','b','c','d','e']
#a) Print the list.
print(letters)

#b) Print the second to last element in the list.
print(letters[-2])

#c) reverse the list
letters.sort(reverse=True)

#d) print the list
print(letters)

#e) print the third to last element in the list.
print(letters[-3])

#f) replace the lowercase letter 'b' with uppercase letter 'B'
letters[-2] = 'B'

#g) replace the lowercase letter 'd' with uppercase letter 'D'
letters[1] = 'D'

#h) print the list.
print(letters)

#i) Alphabetically sort the list.
letters.sort()

#j) Print the list.
print(letters)