from helpers.decorators import input_error
from classes.Record import Record


class ContactsCommands:
    @input_error
    def add_contact(args, book):
        name, phone = args
        record = book.find(name)

        if not record:
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            return f"{name} was added to your book"

        record.add_phone(phone)
        return f"New phone was added to {name}'s record"

    @input_error
    def show_all(args, book):
        return str(book)
