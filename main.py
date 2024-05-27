from h_w_06 import AddressBook, Record
import pickle


def input_error(func):
    def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Give me name and phone please."
            except KeyError:
                return "Contact not found"
            except IndexError:
                return "Not found"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts: AddressBook):
    name, phone = args
    record = contacts.find(name)
    if record is None:
        record = Record(name)
        contacts.add_record(record)
    record.add_phone(phone)
    return "Contact added."

@input_error
def change(args, contacts: AddressBook):
    name, old_phone, new_phone = args
    record = contacts.find(name)
    if record is None:
        return "Contact not found"
    record.edit_phone(old_phone, new_phone)
    return "Contact changed"

@input_error
def phone(args, contacts):
    name = args[0]
    record = contacts.find(name)
    if record is None:
        return "Contact not found"
    else:
        return record

@input_error
def all(args, contacts):
    return contacts

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    record = contacts.find(name)
    if record is None:
        return "Contact not  found"
    record.add_birthday(birthday)
    return "Birthday is added"

@input_error
def show_birthday(args, contacts):
    name = args[0]
    record = contacts.find(name)
    if record is None:
        return "Contact not  found"
    return record.birthday

@input_error
def birthdays(args, contacts: AddressBook):
    return contacts.get_upcoming_birthdays()

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
def main():
    contacts = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(contacts)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change(args, contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "all":
            print(all(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()