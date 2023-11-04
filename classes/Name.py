from classes.Field import Field
from helpers.error import NameValueError


class Name(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(str(value)) <= 1:
            raise NameValueError(
                "Please enter correct name. Name must be more than 1 character.")

        self.__value = value
