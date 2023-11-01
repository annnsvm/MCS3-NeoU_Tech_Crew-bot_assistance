from classes.Email import Email
from classes.Name import Name


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthdays = None
        self.address = None
        self.email = None

    def add_email(self, email):
        self.Email(email)

    def show_email(self, email):
        return self.email
