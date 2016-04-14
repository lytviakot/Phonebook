import functools
import serializators
import json
import pickle

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
    def __init__(self):
        self.contact = input('Enter username: ')
        self.number = input('Enter phone number: ')

   # def __repr__(self):
        #return '{}'.format(self.contact, self.number)


class Phonebook:

    def __init__(self):
        self.contacts = {}

    def __repr__(self):
        return '{}'.format(self.contacts)

    def __str__(self):
        return '{}'.format(self.contacts)

    #add and change - same algorithm
    def add_contact(self, input_contact):
        if input_contact.contact not in self.contacts:
            self.contacts[input_contact.contact] = input_contact.number
        else:
            raise ValueError('Contact is already in phonebook.')

    def delete_contact(self, input_contact):
        del self.contacts[input_contact.contact]

    def show_contact_number(self, input_contact):
        if input_contact.contact not in self.contacts:
            raise ValueError('Contact is already in phonebook.')
        else:
            return '{}'.format(self,input_contact.number)

#serializators.json_serial_save(b)

class UserChoice:

    def __init__(self, phone_book):
        self.operation = input("""Choose action:
        1 - Show phonebook
        2 - Add contact
        3 - Update contact
        4 - Remove contact
        q - Quit
        """)
        self.user_choice = {'2': phone_book.add_contact(), '4': phone_book.delete_contact()}

    def __repr__(self):
        return '{}'.format(self.operation)

    def execute_operation(self):
        if self.operation not in '1234q':
            raise ValueError('Wrong operation code')
        elif self.operation in "Qq":
            exit()
        else:
            self.user_choice[self.operation]()

a = Contact()
b = Phonebook()
b.add_contact(a)
#c = UserChoice(b)
#print(b)
