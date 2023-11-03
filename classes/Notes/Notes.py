from Notes.Notes import InputException, Notebook, RecordNote

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Give me name, please."
        except KeyError:
            return "Contact not found."
        except InputException:
            return "Invalid phone number."
    return inner

def input_error_special(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and two phones, please."
        except IndexError:
            return "Invalid birthday date."
    return inner


def string_reader(user_input, cmd):
    user_input_res = user_input.strip()[len(cmd):]
    text_string = user_input_res[(user_input_res.find('"')) : (len(user_input_res) - user_input_res[::-1].find('"'))]
    part_list = list(user_input_res.partition(text_string))
    text = part_list[1].strip()
    tags = []
    if len(part_list) == 3:
        part_list[2] = part_list[2].split(',')
        name = part_list[0].strip()
        for tag in part_list[2]:
            if len(tag.strip()) > 0:
                tags.append(tag.strip())
        *args , = name, text, tags
    else:
        *args , = name, text
    return cmd, *args ,
    

def parse_input(user_input):
    norm_str = user_input.strip().lower()
    if norm_str.startswith("add note"):
        cmd = "add note"
        return string_reader(user_input, cmd)
        
    elif norm_str.startswith("replace note text"):
        cmd = "replace note text"
        return string_reader(user_input, cmd)
    
    elif norm_str.startswith("add text to note"):
        cmd = "add text to note"
        return string_reader(user_input, cmd)
    
    elif norm_str.startswith("add tags"):
        cmd = "add tags"
        user_input_prep = user_input[len(cmd):].split(':')
        args = []
        tags = []
        if len(user_input_prep) == 2:
            args.append(user_input_prep[0].strip())
            for tag in user_input_prep[1].split(','):
                tags.append(tag.strip())
            args.append(tags)
        else:
            raise InputException
        *args , = args

    elif norm_str.startswith("remove tag"):
        cmd = "remove tag"
        user_input_prep = user_input[len(cmd):].split(':')
        args = []
        if len(user_input_prep) == 2:
            args.append(user_input_prep[0].strip())
            args.append(user_input_prep[1].strip())
        else:
            raise InputException
        *args , = args

    elif norm_str.startswith("show note"):
        cmd = "show note"
        res = user_input.strip()[len(cmd):]
        return cmd, res.strip()

    elif norm_str.startswith("remove note"):
        cmd = "remove note"
        res = user_input.strip()[len(cmd):]
        return cmd, res.strip()
    
    elif norm_str.startswith("find tagged notes"):
        cmd = "find tagged notes"
        res = user_input.strip()[len(cmd):]
        return cmd, res.strip()
    else:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    return cmd, *args


@input_error
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


def remove_note(args, book: Notebook):
    print(args[0])
    note = book.find(args[0])
    if note:
        book.delete(args[0])
    else:
        return "Note not found."


@input_error
def replace_note_text(args, book: Notebook):
    note_name = args[0]
    note_text = args[1]
    note = book.find(note_name)
    if note:
        note.add_note(note_text)
        return "Note text replaced"
    else:
        return "Note not found"


@input_error
def add_note_text(args, book: Notebook):
    note_name = args[0]
    note_text = args[1]
    note = book.find(note_name)
    if note:
        note.add_text(note_text)
        return "Text added"
    else:
        return "Note not found"


@input_error
def add_tag(args, book: Notebook):
    print(args)
    note_name, tags = args
    note = book.find(note_name)
    if note:
        note.add_tag(tags)
        return "New tags added"
    else:
        return "There is no note with that name."


@input_error
def remove_tag(args, book: Notebook):
    name, tag = args
    if not book.find(name):
        return "Tag not found."
    else:
        note = book.find(name)
        note.remove_old_tag(tag)
        return "Tag removed."


@input_error
def get_note(args, book: Notebook):
    note = book.find(args[0])
    if note:
        return note
    else:
        return "Note not found."


@input_error
def get_all(book: Notebook):
    notes_list = []
    if not book.data:
        return "Notes list is empty"
    for name, record in book.data.items():
        notes_list.append(f"{name} : {record}\n")
    return "".join(notes_list)


def all_tags(book: Notebook):
    tag_list = []
    if not book.data:
        return "No tags created"
    for record in book.data.values():
        for tag in record.tags:
            tag_list.append(tag.value)
    return set(tag_list)


def find_tagged_notes(args, book: Notebook):
    notes_list = []
    for name, record in book.data.items():
        for value in record.tags:
            if value.value == args[0]:
                print(name)
                notes_list.append(name)
    return notes_list


@input_error
def show_note(args, book: Notebook):
    my_note = book.find(args[0])
    if my_note and my_note.note_name:
        return my_note.note_text.value
    else:
        return "Note is empty."


def main():
    book: Notebook = Notebook()
    print(''+
        '\nI accept the following commands:'\
        '\n ADD NOTE (title "text" tag, tag)'\
        '\n NOTE (title)'\
        '\n REPLACE NOTE TEXT (title "new text")'\
        '\n ADD TEXT TO NOTE (title "text to add")'\
        '\n ALL ()'\
        '\n ADD TAGS (title : tag, tag)'\
        '\n REMOVE TAG (title : tag)'\
        '\n REMOVE NOTE (title)'\
        '\n SHOW NOTE (title)'\
        '\n FIND TAGGED NOTES (tag)'\
        '\n TAGS ()'\
        '\n CLOSE or EXIT')
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "add note":
            print(add_note_title(args, book))
        elif command == "note":
            print(get_note(args, book))
        elif command == "replace note text":
            print(replace_note_text(args, book))
        elif command == "add text to note":
            print(add_note_text(args, book))
        elif command == "all":
            print(get_all(book))
        elif command == "add tags":
            print(add_tag(args, book))
        elif command == "remove tag":
            print(remove_tag(args, book))
        elif command == "remove note":
            print(remove_note(args, book))
        elif command == "show note":
            print(show_note(args, book))
        elif command == "find tagged notes":
            print(find_tagged_notes(args, book))
        elif command == "tags":
            print(all_tags(book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()