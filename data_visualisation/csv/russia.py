import csv

filename = 'russia.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    for index, header in enumerate(header_row):
        print(index, header)
