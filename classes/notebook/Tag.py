from classes.notebook.Field import Field

class Tag(Field):
    def __init__(self, value):
        if self.validate(value):
            self.value = value
#       else:
#           raise SomeException("some text")

    @staticmethod
    def validate(value):
#       some code
        return True