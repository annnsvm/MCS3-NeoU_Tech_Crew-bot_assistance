from commands.Emails import EmailCommands
from helpers.decorators import parse_input
from classes.AddressBook import AddressBook


def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add-email":
            result = EmailCommands.add_email(args, book)
        elif command == "show-email":
            result = EmailCommands.show_mail(args, book)
        else:
            print("Invalid command.")
        return result


if __name__ == "__main__":
    main()
