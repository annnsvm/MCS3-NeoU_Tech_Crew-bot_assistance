from helpers.decorators import input_error
from helpers.error import PhoneValueError, ContactValueError


class PhoneCommands:
    @input_error
    def show_phone(args, book):
        name = args[0]
        record = book.find(name)

        if not record:
             raise ContactValueError(f"Name {name} is not in the address book")

        if not record.phones:
            raise PhoneValueError(
                f"No phone numbers available for {name} contact.")

        phones = ', '.join(p.value for p in record.phones)
        return f"Phones: {phones}"

    @input_error
    def change_phone(args, book):
        name, old_phone, new_phone = args
        record = book.find(name)

        if not record:
             raise ContactValueError(f"Name {name} is not in the address book")

        record.edit_phone(old_phone, new_phone)
        return f"{name}'s contact is updated"
