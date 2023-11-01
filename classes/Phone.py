from classes.Field import Field


class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not (len(str(value)) == 10 and value.isdigit()):
            raise ValueError(
                "Invalid phone number. The number must contain 10 digits.")

        self.__value = value
