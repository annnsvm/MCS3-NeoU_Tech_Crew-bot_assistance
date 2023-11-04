from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from commands.Birthday import BirthdayCommands
from commands.Emails import EmailCommands
from commands.System import SystemCommands
from commands.Contacts import ContactsCommands
from commands.Phone import PhoneCommands
from commands.Addresses import AddressesCommand
from helpers.decorators import parse_input
from classes.AddressBook import AddressBook

from classes.notebook.Notebook import Notebook
from commands.notebook.Find import FindCommands
from commands.notebook.Note import NoteCommands
from commands.notebook.Tag import TagCommands
from commands.notebook.Text import TextCommands

INFO_PATH = "./data/info.pkl"


def info():
    with open(INFO_PATH, "r") as file:
        return "".join(file.readlines())


command_completer = NestedCompleter.from_nested_dict({
    "info": None,
    "hello": None,
    "close": None,
    "exit": None,
    "all-contacts": None,
    "add-contact": {"<name> <phone>": None},
    "delete-contact": {"<name>": None},
    "show-phone": {"<name>": None},
    "change-phone": {"<name> <old phone> <new phone>": None},
    "add-email": {"<name> <email>": None},
    "show-email": {"<name>": None},
    "add-address": {"<name> <city> <street> <house number>": None},
    "show-address": {"<name>": None},
    "add-birthday": {"<name> <birthday>": None},
    "show-birthday": {"<name>": None},
    "birthdays": None,
    "all-notes": None,
    "add-note": {"<title> '<description>' <tag>, <tag>": None},
    "about-note": {"<title>": None},
    "replace-note-text": {"<title> '<description>'": None},
    "add-text-to-note": {"<title> '<description>'": None},
    "add-tags":  {"<title>: <tag>, <tag>": None},
    "remove-tag": {"<title>: <tag>": None},
})


style = Style.from_dict({
    'completion-menu.completion': 'bg:#feeeb3 #ffffff bold',
    'completion-menu.completion.current': 'bg:#b4effd #000000 bold',
    'scrollbar.background': 'bg:#fdd53f',
    'scrollbar.button': 'bg:#69dffc',
    'prompt': '#00a587',
})

session = PromptSession(completer=command_completer, style=style)


def main():
    book = AddressBook()
    book.load()
    notebook = Notebook()
    notebook.load()
    print("Welcome to the assistant bot!")

    while True:
        result = None
        user_input = session.prompt("Enter a command: ")

        try:
            command, *args = parse_input(user_input)
        except ValueError:
            continue

        if command in ["close", "exit"]:
            result = SystemCommands.show_goodbye()
            book.save()
            notebook.save()
            print(result)
            break

        elif command == "hello":
            result = SystemCommands.show_greeting()
        elif command == "info":
            print(info())
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
            result = EmailCommands.show_email(args, book)
        elif command == "change-email":
            result = EmailCommands.change_email(args, book)
        elif command == "add-birthday":
            result = BirthdayCommands.add_birthday(args, book)
        elif command == "show-birthday":
            result = BirthdayCommands.show_birthday(args, book)
        elif command == "birthdays":
            result =  BirthdayCommands.birthdays(book)
        elif command == "add-address":
            result = AddressesCommand.add_address(args, book)
        elif command == "show-address":
            result = AddressesCommand.show_address(args, book)
        elif command == "all-notes":
            result = FindCommands.get_all(notebook)
        elif command == "add-note":
            result = NoteCommands.add_note_title(args, notebook)
        elif command == "about-note":
            result = FindCommands.get_note(args, notebook)
        elif command == "replace-note-text":
            result = TextCommands.replace_note_text(args, notebook)
        elif command == "add-text-to-note":
            result = TextCommands.add_note_text(args, notebook)
        elif command == "add-tags":
            result = TagCommands.add_tag(args, notebook)
        elif command == "remove-tag":
            result = TagCommands.remove_tag(args, notebook)
        elif command == "remove-note":
            result = NoteCommands.remove_note(args, notebook)
        elif command == "show-note":
            result = FindCommands.show_note(args, notebook)
        elif command == "find-tagged-notes":
            result = FindCommands.find_tagged_notes(args, notebook)
        elif command == "tags":
            result = FindCommands.all_tags(notebook)
        else:
            result = SystemCommands.show_invalid()

        if (result):
            print(result)


if __name__ == "__main__":
    main()
