import pickle
from collections import UserDict

FILE_PATH = "./data/notebook.pkl"

class Notebook(UserDict):
    file_name = "note_data.bin"

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
        
    def add_record(self, record):
        self.data[record.note_name.value] = record

    def find(self, note_name):
        return self.data.get(note_name, None)

    def delete(self, note_name):
        del self.data[note_name]