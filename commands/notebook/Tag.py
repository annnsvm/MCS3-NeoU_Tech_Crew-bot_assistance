from classes.notebook.Notebook import Notebook

def add_tag(args, book: Notebook):
    note_name, tags = args
    note = book.find(note_name)
    if note:
        note.add_tag(tags)
        return "New tags added"
    else:
        return "There is no note with that name."


def remove_tag(args, book: Notebook):
    name, tag = args
    if not book.find(name):
        return "Tag not found."
    else:
        note = book.find(name)
        note.remove_old_tag(tag)
        return "Tag removed."