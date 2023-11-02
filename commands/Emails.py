from helpers.decorators import input_error
from helpers.error import IncorrectEmail


class EmailCommands:
    @input_error
    def add_email(args, book):
        if len(args) != 2:
            return "Give me email please"
        name, email = args
        record = book.find(name)

        if not record:
            raise IncorrectEmail(
                "Please enter correct email.")

        record.add_email(email)
        return "Email was successfully added"

    @input_error
    def show_mail(args, book):
        name = args[0]
        record = book.find(name)

        if not record:
            raise IncorrectEmail(f"Name {name} is not in the address book")

        if not record.email:
            raise IncorrectEmail(
                f"{name} contact does not have email entry")

        return f"Phones: {record.email}"
