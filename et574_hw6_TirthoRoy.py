print("Q1)")
players = {'Adam Vinatieri': 49, 'Trevor Lawrence': 21, 'Kyle Pitts': 22}
def get_youngest_player():
    return min(players, key=players.get)


print(f'The youngest player is {get_youngest_player()}. He is {players[get_youngest_player()]} years old.')

print("\nQ2)")
sh1 = {
    'name': 'Batman',
    'powers': {'Intelligence', 'Technology', 'Science'}
}
sh2 = {
    'name': 'Superman',
    'powers': {'Flight', 'Strength', 'Vision'}}

sh3 = {
    'name': 'Saitama',
    'powers': {'Invincible', 'Absolute Infinite Strength & Speed'}}

superheroes = []
superheroes.append(sh1)
superheroes.append(sh2)
superheroes.append(sh3)
for p in superheroes:
    print(f"{p['name']:6}:", end=" ")
    print(f"{p['powers']}")






print("\nQ3)")
s1 = {
    'name': 'John',
    'grades': [90,84,64]}

s2 = {
    'name': 'Sarah',
    'grades': [73,80,63]}

s3   = {
    'name': 'Lara',
    'grades': [95,72,83]}

students = []
students.append(s1)
students.append(s2)
students.append(s3)


#Remove non passing grades of students
for student in students:
    for grade in student['grades']:
        if grade <=65:
            student['grades'].remove(grade)

#Get average passing grade of students.
for student in students:
    studentName = student["name"]
    passingGrades = student["grades"]
    average = f'{(sum(student["grades"])/(len(student["grades"]))):.2f}'
    print(f'{studentName} {(" ".join(map(str,passingGrades)))} - Avg = {average}')
