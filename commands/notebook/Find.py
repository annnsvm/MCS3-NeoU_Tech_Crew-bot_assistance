from classes.notebook.Notebook import Notebook

def get_note(args, book: Notebook):
    note = book.find(args[0])
    if note:
        return note
    else:
        return "Note not found."


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
                notes_list.append(name)
    return notes_list


def show_note(args, book: Notebook):
    my_note = book.find(args[0])
    if my_note and my_note.note_name:
        return my_note.note_text.value
    else:
        return "Note is empty."