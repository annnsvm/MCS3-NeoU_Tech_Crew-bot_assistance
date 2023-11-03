class IncorrectEmail(Exception):
    def __init__(self, message, *args):
        super().__init__(*args)
        self.message = message


class PhoneValueError(Exception):
    def __init__(self, message, *args):
        super().__init__(*args)
        self.message = message


class NameValueError(Exception):
    def __init__(self, message, *args):
        super().__init__(*args)
        self.message = message


class BirthdayValueError(Exception):
    def __init__(self, value, *args):
        super().__init__(*args)
        self.message = f"Birthday:{value} must be less than current year and date"


class DateValueError(Exception):
    def __init__(self, value, *args):
        super().__init__(*args)
        self.message = f"Wrong birthday date:{value} Please, input DD.MM.YYYY"
