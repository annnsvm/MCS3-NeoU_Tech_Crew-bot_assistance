from datetime import datetime
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
                self.data = pickle.load(file)
        except (EOFError, FileNotFoundError, IOError):
            self.data = {}

    def get_birthdays_for_week(self):
        week_days = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": [],
        }

        today = datetime.today().date()
        birthday_list = []

        for name, record in self.data.items():
            if not record.birthday:
                continue
            birthday_obj = datetime.strptime(
                record.birthday.value, "%d.%m.%Y").date()
            birthday_this_year = birthday_obj.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_obj.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                weekday = birthday_this_year.weekday()
                day_name = ["Monday", "Tuesday", "Wednesday",
                            "Thursday", "Friday", "Saturday", "Sunday"][weekday]
                week_days[day_name].append(name)

        for key, value in week_days.items():
            if value != []:
                birthday_list.append(f"{key}: {', '.join(value)}\n")
        if birthday_list:
            return "".join(birthday_list).removesuffix("\n")
        else:
            return "Next week birthdays not found"

    def save(self):
        with open(FILE_PATH, "wb") as file:
            pickle.dump(self.data, file)

    def __str__(self):
        result = ""
        if len(self.data) == 0:
            result = "Address book is empty."
        else:
            for record in self.data.values():
                result += str(record) + "\n"

        return result.rstrip()
