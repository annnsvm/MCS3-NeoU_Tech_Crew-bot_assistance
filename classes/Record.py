from classes.Email import Email
from classes.Name import Name
from classes.Phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthdays = None
        self.address = None
        self.email = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = Phone(new_phone)
            return

        raise ValueError(
            f"Phone not found")

    def find_phone(self, phone):
        phone = Phone(phone)
        for p in self.phones:
            if p == phone:
                return p
        raise ValueError(f"Phone not found")

    def add_email(self, email):
        self.email = Email(email)

    def show_email(self, email):
        return self.email

    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

        if self.email:
            result += f", email: {str(self.email)}"

        return result
