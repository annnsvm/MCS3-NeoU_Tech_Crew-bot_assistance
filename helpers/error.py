class IncorrectEmail(Exception):
    def __init__(self, message, *args):
        super().__init__(*args)
        self.message = message


class IncorrectAddress(Exception):
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
