from helpers.decorators import input_error
from helpers.error import IncorrectEmail
from helpers.error import ContactValueError

class EmailCommands:
    @input_error
    def add_email(args, book):
        if len(args) != 2:
            return "Give me email please"
        name, email = args
        record = book.find(name)

        if not record:
            raise ContactValueError(f"Name {name} is not in the address book")

        record.add_email(email)
        return "Email was successfully added"

    @input_error
    def show_email(args, book):
        name = args[0]
        record = book.find(name)

        if not record:
            raise ContactValueError(f"Name {name} is not in the address book")

        if not record.email:
            raise IncorrectEmail(
                f"{name} contact does not have email entry")

        return f"Email: {record.email}"
    
    @input_error
    def change_email(args, book):
        name, old_email, new_email = args
        record = book.find(name)
        if not record:
            raise ContactValueError(f"{name} is not in the address book")
        record.edit_email(old_email,new_email)
        return f"{name}'s email is updated"