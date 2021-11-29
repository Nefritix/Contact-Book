import sqlite3

connection = sqlite3.connect('contacts1.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM contacts")
database_list = cursor.fetchall()

    #creating table
def create_table(cursor):
    cursor.execute("""CREATE TABLE contacts (
    first_name text,
    last_name text,
    phone_number text
    )""")


def save_contact(first_name, last_name, phone_number):
    cursor.execute(f"INSERT INTO contacts VALUES ('{first_name}', '{last_name}', '{phone_number}')")
    connection.commit()
    connection.close()


def delete_contact(first_name, last_name):
    cursor.execute(f"DELETE from contacts WHERE first_name = '{first_name}' AND last_name = '{last_name}'")
    connection.commit()
    connection.close()


turn = 1
contact_input = True
contact_input_remove = False
contact_book = {}
command_list = ("Show : displays contact list \nRemove : lets you remove contacts \nAdd : lets you add contacts \nDone : ends program")
print(command_list)

class Person:

    def __init__(self, first, last,  phone_number):
        self.first = first
        self.last = last
        self.phone_number = phone_number

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


while turn == 1:
    first_name = input("What is the first name ").lower()
    if first_name.lower() == "show":
        print(database_list)
        contact_input = False
    elif first_name == "help":
        print(command_list)
        contact_input = False
    elif first_name == "remove":
        contact_input_remove = True
    elif first_name == "done":
        break
    if not contact_input_remove and contact_input:
        last_name = input("What is the last name: ").lower()
        if last_name == "show":
            print(database_list)
            contact_input = False
        elif last_name == "help":
            print(command_list)
            contact_input = False
        elif last_name == "remove":
            contact_input_remove = True
        elif last_name == "done":
            break
    if not contact_input_remove and contact_input:
        phone_number = input("What is that persons number? ").lower()
        if phone_number == "show":
            print(database_list)
            contact_input = False
        elif phone_number == "help":
            print(command_list)
            contact_input = False
        elif phone_number == "remove":
            contact_input_remove = True
        elif phone_number == "done":
            break


    if not contact_input_remove and contact_input:
        contact_book[f"{first_name} {last_name}"] = f" {phone_number}"
        contact_list = Person(first_name.capitalize(), last_name.capitalize(), phone_number)
        save_contact(first_name, last_name, phone_number)
        print("user " + Person.fullname(contact_list) + " has been added to contacts")

    contact_input = True

    while contact_input_remove:
        print(database_list)
        print("You are about to delete a contact")
        first_name = input("what is the first name?: ").lower()


        if first_name == "help":
            print(command_list)
        elif first_name == "add":
            contact_input_remove = False
        elif first_name == "show":
            print(contact_book)
        elif first_name == "done":
            break
        last_name = input("what is the last name? ").lower()

        if last_name == "help":
            print(command_list)
        elif last_name == "add":
            contact_input_remove = False
        elif last_name == "show":
            print(contact_book)
        elif last_name == "done":
            break
        else:
            try:
                delete_contact(first_name, last_name)
            except:
                print("did not find name ")
