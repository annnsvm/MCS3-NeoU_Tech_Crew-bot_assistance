from commands.Emails import EmailCommands
from commands.System import SystemCommands
from commands.Contacts import ContactsCommands
from helpers.decorators import parse_input
from classes.AddressBook import AddressBook


def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")

    while True:
        result = None
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            result = SystemCommands.show_goodbye()
            print(result)
            break

        elif command == "hello":
            result = SystemCommands.show_greeting()
        elif command == "add":
            result = ContactsCommands.add_contact(args, book)
        elif command == "all":
            result = ContactsCommands.show_all(args, book)
        elif command == "add-email":
            result = EmailCommands.add_email(args, book)
        elif command == "show-email":
            result = EmailCommands.show_mail(args, book)
        else:
            print("Invalid command.")
        if (result):
            print(result)


if __name__ == "__main__":
    main()
