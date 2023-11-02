from classes.Field import Field
from helpers.error import IncorrectEmail


class Email(Field):
    def __init__(self, value):
        if '@' not in value or '.' not in value.split('@'-1) or ' ' in value:
            raise ValueError('Invalid email address')
        super.__init__(value)
