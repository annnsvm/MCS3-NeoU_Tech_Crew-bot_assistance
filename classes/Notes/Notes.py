from collections import UserDict

# Спільний блок
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Блок для відображення помилок

def input_notebook_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InputException:
            return "Please enter the data correctly. For a hint, type 'help'"
    return inner


class InputException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


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

    def remove_old_tag(self, tags):
        tag_name = tags[0]
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
        return f"Note name: {self.note_name.value}\
        tags: {', '.join(t.value for t in self.tags)}, \
        Note: {self.note_text.value if self.note_text else 'No notes'}"


class Notebook(UserDict):
    def add_record(self, record):
        self.data[record.note_name.value] = record

    def find(self, note_name):
        return self.data.get(note_name, None)

    def delete(self, note_name):
        del self.data[note_name]


def cmd_and_string_reader(user_input):
    separator = user_input.find(" ")
    cmd = user_input[:separator].strip().lower()
    prep_str = user_input[separator:].strip()
    return cmd, prep_str


def string_reader(prep_str):
    tags = []
    text = ""
    if prep_str.find('"') != -1 and prep_str.find('"') != prep_str[::-1].find('"'):
        text_string = prep_str[(prep_str.find('"')) : (len(prep_str) - prep_str[::-1].find('"'))]
        part_list = list(prep_str.partition(text_string))
        text = part_list[1].strip()
        text = text[1:len(text)-1]
        part_list[2] = part_list[2].split(',')
        name = part_list[0].strip()
        for tag in part_list[2]:
            if len(tag.strip()) > 0:
                tags.append(tag.strip())
    else:
        name = prep_str
    *args , = name, text, tags
    return *args ,


def tag_reader(prep_str):
        prep_list = prep_str.split(':')
        args = []
        tags = []
        if len(prep_list ) == 2:
            args.append(prep_list [0].strip())
            for tag in prep_list [1].split(','):
                tags.append(tag.strip())
            args.append(tags)
        else:
            raise InputException
        return args
    

@input_notebook_error
def parse_input(user_input):
    cmd = (cmd_and_string_reader(user_input))[0]
    prep_str = (cmd_and_string_reader(user_input))[1]
    if cmd == "add-note" or cmd == "replace-note-text" or cmd == "add-text-to-note":
        *args , = string_reader(prep_str)
        return cmd, *args
    elif cmd == "add-tags" or cmd == "remove-tag":
        *args , = tag_reader(prep_str)
        return cmd, *args
    elif cmd == "show-note" or cmd == "remove-note" or cmd == "find-tagged-notes" or cmd == "about-note":
        return cmd, prep_str
    else:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    return cmd, *args


@input_notebook_error
def add_note_title(args, book: Notebook):
    note_name, note_text, note_tags = args
    note = book.find(note_name)
    if note:
        return "Note already exists"
    record = RecordNote(note_name)
    record.add_note(note_text)
    record.add_tag(note_tags)
    book.add_record(record)
    return "Note entry created."


@input_notebook_error
def remove_note(args, book: Notebook):
    note = book.find(args[0])
    if note:
        book.delete(args[0])
    else:
        return "Note not found."


@input_notebook_error
def replace_note_text(args, book: Notebook):
    note_name = args[0]
    note_text = args[1]
    note = book.find(note_name)
    if note:
        note.add_note(note_text)
        return "Note text replaced"
    else:
        return "Note not found"


@input_notebook_error
def add_note_text(args, book: Notebook):
    note_name = args[0]
    note_text = args[1]
    note = book.find(note_name)
    if note:
        note.add_text(note_text)
        return "Text added"
    else:
        return "Note not found"


@input_notebook_error
def add_tag(args, book: Notebook):
    note_name, tags = args
    note = book.find(note_name)
    if note:
        note.add_tag(tags)
        return "New tags added"
    else:
        return "There is no note with that name."


@input_notebook_error
def remove_tag(args, book: Notebook):
    name, tag = args
    if not book.find(name):
        return "Tag not found."
    else:
        note = book.find(name)
        note.remove_old_tag(tag)
        return "Tag removed."


@input_notebook_error
def get_note(args, book: Notebook):
    note = book.find(args[0])
    if note:
        return note
    else:
        return "Note not found."


@input_notebook_error
def get_all(book: Notebook):
    notes_list = []
    if not book.data:
        return "Notes list is empty"
    for name, record in book.data.items():
        notes_list.append(f"{name} : {record}\n")
    return "".join(notes_list)


@input_notebook_error
def all_tags(book: Notebook):
    tag_list = []
    if not book.data:
        return "No tags created"
    for record in book.data.values():
        for tag in record.tags:
            tag_list.append(tag.value)
    return set(tag_list)


@input_notebook_error
def find_tagged_notes(args, book: Notebook):
    notes_list = []
    for name, record in book.data.items():
        for value in record.tags:
            if value.value == args[0]:
                notes_list.append(name)
    return notes_list


@input_notebook_error
def show_note(args, book: Notebook):
    my_note = book.find(args[0])
    if my_note and my_note.note_name:
        return my_note.note_text.value
    else:
        return "Note is empty."


def main():
    notebook: Notebook = Notebook()
    print('Greeting! To see a list of commands, type "help"')
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "add-note":
            print(add_note_title(args, notebook))
        elif command == "about-note":
            print(get_note(args, notebook))
        elif command == "replace-note-text":
            print(replace_note_text(args, notebook))
        elif command == "add-text-to-note":
            print(add_note_text(args, notebook))
        elif command == "all-notes":
            print(get_all(notebook))
        elif command == "add-tags":
            print(add_tag(args, notebook))
        elif command == "remove-tag":
            print(remove_tag(args, notebook))
        elif command == "remove-note":
            print(remove_note(args, notebook))
        elif command == "show-note":
            print(show_note(args, notebook))
        elif command == "find-tagged-notes":
            print(find_tagged_notes(args, notebook))
        elif command == "tags":
            print(all_tags(notebook))
        elif command == "help":
            print(('I accept the following commands:'+
        '\n add-note (title "text" tag, tag)'\
        '\n about-note (title)'\
        '\n replace-note-text (title "new text")'\
        '\n add-text-to-note (title "text to add")'\
        '\n all-notes'\
        '\n add-tags (title : tag, tag)'\
        '\n remove-tag (title : tag)'\
        '\n remove-note (title)'\
        '\n show-note (title)'\
        '\n find-tagged-notes (tag)'\
        '\n tags'\
        '\n close or exit'))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()