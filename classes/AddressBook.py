from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        result = ""
        if len(self.data) == 0:
            result = "Address book is empty."
        else:
            for record in self.data.values():
                result += str(record) + "\n"

        return result.rstrip()
