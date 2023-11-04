from classes.Field import Field
from datetime import date, datetime

from helpers.error import BirthdayValueError, DateValueError


class Birthday(Field):
    def __init__(self, value):
        self.birthday_validation(value)
        super().__init__(value)

    @property
    def birthday(self):
        raise AttributeError('This property has no getter')

    @birthday.setter
    def birthday(self, value):
        self.__init__(value)

    def birthday_validation(self, value):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise DateValueError(value)
        else:
            if birthday_date > date.today():
                raise BirthdayValueError(value)

    def __str__(self):
        return self.value
