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


def main():
    book = AddressBook()
    book.load()
    notebook = Notebook()
    notebook.load()
    print("Welcome to the assistant bot!")

    while True:
        result = None
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            result = SystemCommands.show_goodbye()
            book.save()
            notebook.save()
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
        elif command == "add-address":
            result = AddressesCommand.add_address(args, book)
        elif command == "show-address":
            result = AddressesCommand.show_address(args, book)
        elif command == "add-note":
            result = NoteCommands.add_note_title(args, notebook)
        elif command == "about-note":
            result = FindCommands.get_note(args, notebook)
        elif command == "replace-note-text":
            result = TextCommands.replace_note_text(args, notebook)
        elif command == "add-text-to-note":
            result = TextCommands.add_note_text(args, notebook)
        elif command == "all-notes":
            result = FindCommands.get_all(notebook)
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
    