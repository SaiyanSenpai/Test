from pstats import Stats


print("1")
Countries = {
    'USA': {'Capital':"Washington"},
    'France': {'Capital':'Paris'},
    'India': {'Capital':'New Delhi'}
}
print(Countries)
for Country in Countries.items():
    print(f'The capital of {Country[0]} is {Country[1]["Capital"]}.')

print("\n2")
StudentMajors = {
    'Dembe': 'History',
    'Kate': 'Anthropology'
}
StudentHobbies = {
    'Dembe': ['judo','chess','drawing'],
    'Kate': ['bird-watching','stained-glass','poetry','skating']
}
print(StudentHobbies)

print("\n3")
Alaska = {'capital':'Juneau','population':'731545','size':'665000'}
Hawaii = {'capital':'Honolulu','population':'1415872','size':'10931'}
States = (Alaska,Hawaii)
print(States)

