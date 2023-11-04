from classes.Field import Field
from helpers.error import IncorrectAddress


class Address(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not new_value:
            raise IncorrectAddress('Address cannot be empty')
        self.__value = new_value
