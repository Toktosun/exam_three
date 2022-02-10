import csv

filename = "Data.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))
print('Field names are:' + ', '.join(field for field in fields))
print('Первые 5 строк:')

for row in rows[:5]:
    for col in row:
        print("%10s" % col),


# import csv

# fields = ['Name', 'Surname', 'Year']

# rows = [['Atai', 'Askarov', '2003'],
#         ['Ikhtiyar', 'Rakhimov', '2004']]

# filename = "Data.csv"

# with open(filename, 'w') as csvfile:

#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)
