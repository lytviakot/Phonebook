import sqlite3


class Contact:

    def __init__(self):
        self.contact = input('Enter username: ')
        self.number = input('Enter phone number: ')


class Phonebook:

    db = sqlite3.connect('Phonebook.sqlite3')
    c = db.cursor()

    def __init__(self):
        pass
        #self.contacts = Phonebook.c.execute('select * from PhoneBook')

    #def __repr__(self):
        #return repr(self.contacts)

    #def __str__(self):
        #return '{}'.format(self.contacts)

    @staticmethod
    def create_table():
        Phonebook.c.execute('create table PhoneBook (id integer primary key autoincrement,'
                            ' name varchar(20), number integer)')

    def add_contact(self, Contact):
        Phonebook.c.execute("insert into PhoneBook (name, number) values ('{}', '{}')"
                            .format(Contact.contact, Contact.number))

    def show_contacts(self):
        #by row
        print(Phonebook.c.execute("select * from PhoneBook"))
        print(Phonebook.c.fetchall())

    def delete_contact(self):
        input_contact = input("What contact do u want do delete? ")
        Phonebook.c.execute("delete from PhoneBook where name='{}'".format(input_contact))


a = Contact()
b = Phonebook()
b.add_contact(a)
b.show_contacts()
b.delete_contact()
