import csv
import operator


class CsvWork:

    def __init__(self, data):
        self.data = data

    def sort_one(self):

        with open('dict.csv') as f:
            csv_reader = csv.reader(f, delimiter=';')
            print(sorted(csv_reader, key=operator.itemgetter(1)))

    def add_row_csv(self):
        with open('dict.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow((self.data['first_name'], self.data['last_name'], self.data['age'], self.data['gender'],
                             self.data['hobby'], self.data['job']))
            f.close()

    def update_line(self):

        row_num = 1
        new_value = 'Replaced Line'

        with open('dict.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=';')
            lines = []

            for current_line in csv_reader:
                if csv_reader.line_num == row_num:
                    current_line = new_value
                lines.append(current_line)

        with open('dict.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(lines)

    def edit_line(self):
        line_to_editing = []
        with open('dict.csv') as f:
            csv_reader = csv.reader(f, delimiter=';')
            for row in csv_reader:
                line_to_editing.append(row)
        print(line_to_editing)


jason = {'first_name': 'Beksultan', 'last_name': 'Iskenderov', 'age': 29, 'gender': 'male', 'hobby': 'video games',
         'job': 'QA'}
alice = {'first_name': 'Atay', 'last_name': 'Askarov', 'age': 21, 'gender': 'female', 'hobby': 'sport',
         'job': 'software engineer'}
almaz = {'first_name': 'Ikhtiyar', 'last_name': 'Rakhimov', 'age': 17, 'gender': 'male', 'hobby': 'sport',
         'job': 'software engineer'}

work = CsvWork(beksultan)
work1 = CsvWork(atay)
work.add_row_csv()
work1.add_row_csv()
work.edit_line()
work.sort_one()
work2 = CsvWork(ikhtiyar)
work2.update_line()
