from classes.Field import Field
from datetime import date, datetime

from helpers.error import BirthdayValueError, DateValueError



class Birthday(Field):
    def __init__(self, birthday):
        self.birthday_validation(birthday)
        super().__init__(birthday)


    @property
    def birthday(self):
        raise AttributeError('This property has no getter')

    @birthday.setter
    def birthday(self, birthday):
        self.__init__(birthday)

    def birthday_validation(self, birthday):
        try:
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y").date()
        except ValueError:
            raise DateValueError
        else:
            if birthday_date > date.today():
                raise BirthdayValueError
