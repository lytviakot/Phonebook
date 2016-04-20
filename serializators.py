import json
import csv


'''def serialization(operation):
    def wrapper(user):
        operation(user)
        i = input("""What serialization method to use?
        1 - JSON
        2 - CSV""")
        if i not in '12':
            exit()
        elif i == '1':
            json_serial_save()
            f = open('phonebook.json', 'r')
            return f.read()
        else:
            csv_serial_save()
            f = open('phonebook.csv', 'r')
            return f.read()
    return wrapper'''


class Serializers:

    def json_serial_save(self, source):
        with open('phonebook.json', 'w') as phonebook_json:
            json.dump(source, phonebook_json)

    def json_serial_load(self):
        with open('phonebook.json', 'r') as phonebook_json:
            return json.load(phonebook_json)

    '''   def csv_serial_save(self, source):
        with open('phonebook.csv', 'wb') as phonebook_csv:
            csv.dump(source, phonebook_csv)

    def csv_serial_load(self):
        with open('phonebook.csv', 'wb') as phonebook_csv:
            return csv.load(phonebook_csv)'''