from collections import UserDict

class Notebook(UserDict):
    def add_record(self, record):
        self.data[record.note_name.value] = record

    def find(self, note_name):
        return self.data.get(note_name, None)

    def delete(self, note_name):
        del self.data[note_name]