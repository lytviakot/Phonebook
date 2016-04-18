import os


class Phonebook:

    def __init__(self):
        self.phonebook = {}
        self.phonebook_file = 'Phonebook.txt'

    def file_to_dict(self):
        self.phonebook.clear()

        file = open(self.phonebook_file, 'r')
        for line in file.readlines():
            name, number = line.strip().split()
            self.phonebook[name] = number
        file.close()

    def add_contact(self):
        self.file_to_dict()

        name = input("Enter username: ")
        number = input("Enter number: ")

        new_entry = name + '\t' + number + '\n'
        file = open(self.phonebook_file, 'w')
        file.write(new_entry)
        file.close()

    def show_phonebook(self):
        self.file_to_dict()
        #for name, number in self.phonebook.items():
            #print(name, " : ", number)
        print(self.phonebook)
        if len(self.phonebook) == 0:
            print("Phonebook is empty")

    def find_contact(self):
        self.file_to_dict()
        search = input("Enter contact to search for: ")
        if search in self.phonebook.keys():
            print(search, " : ", self.phonebook[search])
        else:
            print("No such contact")

    def delete_contact(self):
        self.file_to_dict()
        entry_to_delete = input("Emter contact name to delete: ")
        if entry_to_delete in self.phonebook.keys():
            del self.phonebook[entry_to_delete]

            file = open(self.phonebook_file, 'w')
            for name, number in self.phonebook.items():
                string = name + '\t' + number + '\n'
                file.write(string)
            file.close()
            print("Contact deleted")
        else:
            print("No such contact")

    def user_choice(self):
        print("""\
        1) Show all contacts
        2) Add new contact
        3) Delete contact
        4) Find a contact
        5) Exit\n""")
        choice = input("Make your choice: ")
        choice_menu = {'1': self.show_phonebook,
                       '2': self.add_contact,
                       '3': self.delete_contact,
                       '4': self.find_contact,
                       '5': exit()}
        if choice not in choice_menu.keys():
            print("Make your choice: ")
        else:
            choice_menu[choice]()


My_Phonebook = Phonebook()
#My_Phonebook.add_contact()
My_Phonebook.user_choice()