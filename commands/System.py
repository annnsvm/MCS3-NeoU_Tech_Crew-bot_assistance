from helpers.decorators import input_error
from classes.Record import Record


class SystemCommands:
    @input_error
    def show_greeting():
        return "How can I help you?"

    @input_error
    def show_goodbye():
        return "Good bye!"
