from collections import UserDict
from classes.Field import Field


# Блок для відображення помилок
class InputException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# для відображення помилок у валідації тексту що йде в нотатки, ілюстративно
def notes_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InputException:
            return "Please enter the data correctly. For a hint, type 'help' before the command"
    return inner
# кінець блоку


# Класи для нотаток
class Name(Field):
    pass


class Tag(Field):
    def __init__(self, value):
        if self.validate(value):
            self.value = value
#        else:
#            raise SomeException("some text")

    @staticmethod
    def validate(value):
        # some code (Якийсь валідатора тексту, типу не більше 100 символів абощо. Краще через property)
        return True


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

class RecordNote:
    def __init__(self, name):
        self.note_name = Name(name)
        self.tags = []
        self.note_text = None
        
    def add_tag(self, tags):
        for tag in tags:
            self.tags.append(Tag(tag))

    def remove_old_tag(self, tag_name):
        for i, tag in enumerate(self.tags):
            if tag.value == tag_name:
                del self.tags[i]
                return "Tag removed."
        raise ValueError("Tag not found.")

    def find_tag(self, tag_name):
        for tag in self.tags:
            if tag.value == tag_name:
                return tag

    def add_note(self, note_text):
        self.note_text = Note(note_text)
        return "Note added"
    
    def add_text(self, new_text):
        self.note_text.value += new_text
        return "The text has been updated"

    def __str__(self):
        return f"Note name: {self.note_name.value},\
        tags: {', '.join(t.value for t in self.tags)}, \
        Note: {self.note_text.value if self.note_text else 'No notes'}"


class Notebook(UserDict):
    def add_record(self, record):
        self.data[record.note_name.value] = record

    def find(self, note_name):
        return self.data.get(note_name, None)

    def delete(self, note_name):
        del self.data[note_name]