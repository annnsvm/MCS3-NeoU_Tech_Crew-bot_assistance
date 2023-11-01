from helpers.decorators import input_error


class EmailCommands:

    @input_error
    def add_email(args, book):
        if len(args) != 2:
            return "Give me email please"
        name, email = args
        record = book.find(name)
        record.add_email(email)
        return "Email was successfully added"

    @input_error
    def show_mail(args, book):
        name = args[0]
        record = book.find(name)
        email = record.show_email()
        if email:
            return email
        else:
            return "Email not found for this contact"
