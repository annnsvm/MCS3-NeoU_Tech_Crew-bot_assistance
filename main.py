from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession, print_formatted_text, HTML
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

from commands.Birthday import BirthdayCommands
from commands.Emails import EmailCommands
from commands.System import SystemCommands
from commands.Contacts import ContactsCommands
from commands.Phone import PhoneCommands
from commands.Addresses import AddressesCommand
from helpers.decorators import parse_input
from classes.AddressBook import AddressBook


command_completer = WordCompleter([
    'add', 'all', 'show-phone', 'change-phone',
    'add-email', 'show-email', 'add-birthday',
    'show-birthday', 'birthdays', 'hello',
    'close', 'exit'
], ignore_case=True)

style = Style.from_dict({
    'greeting': 'ansigreen',
    'error': 'ansired bold',
    'command': 'ansiblue',
    'result': 'ansiwhite',
})
session = PromptSession(completer=command_completer, style=style)


def main():
    book = AddressBook()
    book.load()
    print("Welcome to the assistant bot!")

    while True:
        result = None
        user_input = session.prompt("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            result = SystemCommands.show_goodbye()
            book.save()
            print(result)
            break

        elif command == "hello":
            result = SystemCommands.show_greeting()
        elif command == "add":
            result = ContactsCommands.add_contact(args, book)
        elif command == "all":
            result = ContactsCommands.show_all(book)
        elif command == "show-phone":
            result = PhoneCommands.show_phone(args, book)
        elif command == "change-phone":
            result = PhoneCommands.change_phone(args, book)
        elif command == "add-email":
            result = EmailCommands.add_email(args, book)
        elif command == "show-email":
            result = EmailCommands.show_mail(args, book)
        elif command == "add-birthday":
            result = BirthdayCommands.add_birthday(args, book)
        elif command == "show-birthday":
            result = BirthdayCommands.show_birthday(args, book)
        elif command == "birthdays":
            print(BirthdayCommands.birthdays(book))
        elif command == "add-address":
            result = AddressesCommand.add_address(args, book)
        elif command == "show-address":
            result = AddressesCommand.show_address(args, book)
        else:
            result = SystemCommands.show_invalid()

        if (result):
            print(result)


if __name__ == "__main__":
    main()
