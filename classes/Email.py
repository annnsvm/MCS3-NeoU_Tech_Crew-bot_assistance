import re
from classes.Field import Field
from helpers.error import IncorrectEmail


class Email(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        r = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(r, value):
            raise IncorrectEmail(
                "Please enter correct email.")

        self.__value = value
