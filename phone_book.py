import functools
import serializators


'''def user_input_decorator(function):
    """Decorator to get username and check it"""
    @functools.wraps(function)
    def wrapper():
        username_input = get_username()
        if not username_input:
            raise ValueError('No contact name entered. Exit.')
        #elif not phone_input:
            #raise ValueError('No contact number entered. Exit.')
        else:
            function(username_input)
    return wrapper


def get_username():
    """Get username using console input"""
    return input('Enter username: ')


def get_number():
    """Get number using console input"""
    return input('Enter number: ')'''


class Contact:

    #@user_input_decorator
    def __init__(self, contact, number):
        self.contact = contact
        self.number = number


def get_information():
    contact = input('Enter username: ')
    number = input('Enter phone number: ')
    return contact, number


def create_contact():
    return Contact(*get_information())


class Phonebook:

    def __init__(self):
        self.contacts = {}

    def __repr__(self):
        return '{}'.format(self.contacts)

    #add and change - same algorithm
    def add_contact(self, input_contact):
        if input_contact.contact not in self.contacts:
            self.contacts[input_contact.contact] = input_contact.number
        else:
            raise ValueError('Contact is already in phonebook.')

    def delete_contact(self, input_contact):
        del self.contacts[input_contact.contact]

    def show_number_by_user(self, input_contact):
        if input_contact.contact in self.contacts:
            self.contacts[input_contact.contact] = input_contact.number
        else:
            raise ValueError('There is no such contact in phonebook.')

    def show_contacts(self):
        if self.contacts:
            print(self.contacts)
        else:
            raise ValueError('The phonebook is empty.')

a = create_contact()
b = Phonebook()
#print(b)

class UserChoice:

    def __init__(self, phonebook):
        self.operation = input("""Choose action:
        1 - Show phonebook
        2 - Add contact
        3 - Update contact
        4 - Remove contact
        q - Quit
        """)
        self.user_choice = {'1': phonebook.show_contacts, '2': phonebook.add_contact, '4': phonebook.delete_contact}

    def __repr__(self):
        return '{}'.format(self.operation)

    def execute_operation(self):
        if self.operation not in '1234q':
            raise ValueError('Wrong operation code')
        elif self.operation in "Qq":
            exit()
        else:
            self.user_choice[self.operation]()

UserChoice(b)