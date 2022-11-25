# csv writer and writerow
import csv

castaway=[4, "Castaway", "Chuck Noland"]

with open('data/write_csv.csv', 'w',) as file:
    writer = csv.writer(file)
    #print(type(writer))
    writer.writerow(["Record#", "Film", "Lead Character"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])
    writer.writerow([3, "Scaramouche", "Andrei Moreau"])
    writer.writerow(castaway)
print('The file has been written.')

#https://www.programiz.com/python-programming/csv
