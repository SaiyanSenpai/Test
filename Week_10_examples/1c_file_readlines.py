# readlines() produces a list

'''csv files are comma-separated value files.
   The ',' is the delimiter. It separates the data.
   The first row of a csv file usually stores the headers.
   The rows that follow can be thought of as individual records.
   csv files can be opened in Spreadsheet software such as Excel.
   https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
   '''

filename = 'data/states.csv'

# readlines() returns a list from the 'file_object'
with open(filename, 'r') as file_object:
    my_data = file_object.readlines()
print(my_data)
# print the list
for d in my_data:
    print(d)
'''
# print the list rawData (remove the trailing blank lines)
for d in my_data:
    print(d.rstrip())    # strip the trailing blank lines
print('')
'''
