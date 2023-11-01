from classes.Field import Field


class Name(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(str(value)) == 0:
            raise ValueError("Please enter name")

        self.__value = value
