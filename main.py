from commands.Emails import EmailCommands
from commands.System import SystemCommands
from commands.Contacts import ContactsCommands
from commands.Phone import PhoneCommands
from helpers.decorators import parse_input
from classes.AddressBook import AddressBook


def main():
    book = AddressBook()
    book.load()
    print("Welcome to the assistant bot!")

    while True:
        result = None
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            result = SystemCommands.show_goodbye()
            book.save()
            print(result)
            break

        elif command == "hello":
            result = SystemCommands.show_greeting()
        elif command == "add-contact":
            result = ContactsCommands.add_contact(args, book)
        elif command == "delete-contact":
            result = ContactsCommands.delete_contact(args, book)
        elif command == "all-contacts":
            result = ContactsCommands.show_all_contacts(book)
        elif command == "show-phone":
            result = PhoneCommands.show_phone(args, book)
        elif command == "change-phone":
            result = PhoneCommands.change_phone(args, book)
        elif command == "add-email":
            result = EmailCommands.add_email(args, book)
        elif command == "show-email":
            result = EmailCommands.show_mail(args, book)
        else:
            result = SystemCommands.show_invalid()

        if (result):
            print(result)


if __name__ == "__main__":
    main()
