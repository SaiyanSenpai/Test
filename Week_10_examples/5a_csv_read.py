#read a csv file using csv.reader()
import csv
with open('data/55aschool.csv', 'r') as file:
    reader = csv.reader(file)
    print(next(reader)) #print the header
    #print(next(reader)) #print first record
    #print(next(reader)) #print first record
#print the records/observations
    for row in reader:
        print(row)
