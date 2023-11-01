from classes.Field import Field

class Note(Field):
    def __init__(self, value):
        if self.validate(value):
            self.value = value
#        else:
#            raise SomeException("some text")

    @staticmethod
    def validate(value):
        # some code (Якийсь валідатора тексту, типу не більше 100 символів абощо. Краще через property)
        return True