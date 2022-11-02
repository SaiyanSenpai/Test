# ET574 Python Exam 1   ### Tirtho Roy ###
print ('Q1')
names = ['Bird', 'Bryant', 'Ewing', 'Jordan', 'Maravich']
print(sorted(names, reverse = True))

print('\nQ2')
name_list = ["Jordan", "Bird", "Bryant", "Maravich", "Ewing"]
last_3_elements = slice(2,5)
print(sorted(name_list[last_3_elements]))

print('\nQ3')
print('The 4 most popular programming languages of 2022 are:\n1.\tPython\n2.\tJavascript\n3.\tJava\n4.\tC#')

print('\nQ4')
temps = [56,65,47,74,38,83]
print(min(temps),max(temps),(sum(temps)/(len(temps))))

print('\nQ5')
print((23/3)%1)

print('\nQ6')
pets = ['teddy','polly','jessie','ghost']
print(f'Hello {str.upper(pets[pets.index("polly")])}, you are a fine parrot!')

print('\nQ7')
pets.insert(1,'spot')
print(pets)

print('\nQ8')
pets_in_heaven = pets[pets.index('teddy'):pets.index('teddy')+1]+pets[pets.index('jessie'):pets.index('jessie')+1]
print(pets_in_heaven)

print('\nQ9')
instruments = ['guitar','pinao','violin']
for instrument in instruments:
    print(f'I love to play the {instrument}')

print('\nQ10')
multiples = list(range(0,5*11,5))
print(f'{multiples}\n{sum(multiples)}')

print('\nQ11')
gpa = 3.8
def check_gpa(num):
    if num>=3.5:
        print("You are a great student!")
    elif num>=2.5 and num<3.5:
        print("You are a good student!")
    else:
        print("You really need to study more!")
check_gpa(gpa)

print('\nQ12')
metals = ['tin', 'copper', 'brass', 'gold', 'iron']
for metal in metals:
    if metal == "gold":
        print("Gold, Gold, I'm rich, I'm rich!")
    else:
        print(f"Darn {metal.title()} I have no luck")

print('\nQ13 extra-credit')
names=['Joe', 'Amy', 'Lil', 'Poe', 'Ali', 'Sid']
grades=[65, 63, 89, 96, 59, 81] 

for student_name in names:
    index_num = names.index(student_name)
    if grades[index_num] >=65:
        print(f'{student_name.title()}, you passed!')
    else:
        print(f'{student_name.title()}, you need to study more!')

print('\nQ14 extra-credit')
fruits = ['apple','banana','cherry']
descriptions = ['sweet','tasty']
for taste in descriptions:
    for fruit in fruits:
        print(f'{taste} {fruit}')