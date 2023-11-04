import pickle
from collections import UserDict


FILE_PATH = "./data/address-book.pkl"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def load(self):
        try:
            with open(FILE_PATH, "rb") as file:
                file_content = pickle.load(file)
                self.data = file_content
        except (EOFError, FileNotFoundError, IOError):
            self.data = {}

    def save(self):
        with open(FILE_PATH, "wb") as file:
            pickle.dump(self, file)

    def __str__(self):
        result = ""
        if len(self.data) == 0:
            result = "Address book is empty."
        else:
            for record in self.data.values():
                result += str(record) + "\n"

        return result.rstrip()
