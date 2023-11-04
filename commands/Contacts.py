from helpers.decorators import input_error
from classes.Record import Record


class ContactsCommands:

    def show_all(book):
        if not book:
            return "Your phone book is empty."
        return str(book)

    @input_error
    def add_contact(args, book):
        name, phone = args
        record = book.find(name)

        if not record:
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            return f"{name} is added to the address book"

        record.add_phone(phone)
        return f"New phone is added to {name}'s record"

    @input_error
    def find_contact(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        return book.find_record(name)

    # @input_error
    # def show_all(book):
    #     return str(book)
