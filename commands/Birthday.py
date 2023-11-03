from helpers.decorators import input_error


class BirthdayCommands:
    @input_error
    def add_birthday(args, book):
        if len(args) != 2:
            return "Give me name and birthday please."

        name = args[0]
        birthday = args[1]
        contact = book.find(name)
        if contact:
            contact.add_birthday(birthday)
            return "Birthday added."
        else:
            return f"Contact: {name} not found!"

    @input_error
    def show_birthday(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        contact = book.find(name)
        if contact and contact.birthday:
            return contact.birthday.value
        else:
            return "Birthday not found."

    @input_error
    def birthdays(book):
        return book.get_birthdays_per_week()
