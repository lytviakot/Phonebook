import serializators

saved_contacts = serializators.Serializers()

class Contact:

    def __init__(self):
        self.contact = input('Enter username: ')
        self.number = input('Enter phone number: ')

    def __repr__(self):
        return '{}'.format(self.contact, self.number)


class Phonebook:

    def __init__(self):
        self.contacts = saved_contacts.json_serial_load()

    def __repr__(self):
        return repr(self.contacts)

    def __str__(self):
        return '{}'.format(self.contacts)

    def add_contact(self):
            a = Contact()
            if a.contact not in self.contacts:
                self.contacts[a.contact] = a.number
                saved_contacts.json_serial_save(self.contacts)
            else:
                raise ValueError('Contact is already in phonebook.')

    def delete_contact(self):
        input_contact = input("What contact do u want do delete? ")
        if input_contact in self.contacts:
            del self.contacts[input_contact]
        else:
            raise ValueError('No such contact.')

    def show_number_by_name(self):
        input_contact = input("What contact do u want do delete? ")
        if input_contact not in self.contacts:
            raise ValueError('Contact is already in phonebook.')
        else:
            return '{}'.format(self, self.contacts[input_contact]())

    def show_phonebook(self):
        print(saved_contacts.json_serial_load())
        #return saved_contacts


class UserChoice:

    def __init__(self):
        self.operation = input("""Choose action:
        1 - Show phonebook
        2 - Add contact
        3 - Show number by name
        4 - Remove contact
        q - Quit
        """)

    def execute_operation(self, phone_book):
        user_choice = {'1': phone_book.show_phonebook(), '2': phone_book.add_contact(),
                       '3': phone_book.show_number_by_name(), '4': phone_book.delete_contact()}
        if self.operation not in '1234Qq':
            raise ValueError('Wrong operation code')
        elif self.operation in "Qq":
            exit()
        else:
            user_choice[self.operation]()

b = Phonebook()
u = UserChoice()
u.execute_operation(b)

#b.add_contact()
#print(b.contacts)
#s1 = serializators.Serializers()
#s1.json_serial_save(b.contacts)
#s2 = serializators.Serializers()
#print(type(s2.json_serial_load()))'''