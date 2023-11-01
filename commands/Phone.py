from helpers.decorators import input_error
from helpers.error import PhoneValueError


class PhoneCommands:
    @input_error
    def show_phone(args, book):
        name = args[0]
        record = book.find(name)

        if not record:
            raise PhoneValueError(f"Name {name} is not in the address book")

        return str(record)

    @input_error
    def change_phone(args, book):
        name, old_phone, new_phone = args
        record = book.find(name)

        if not record:
            raise PhoneValueError(f"Name {name} is not in the address book.")

        record.edit_phone(old_phone, new_phone)
        return f"{name}'s contact is updated"
