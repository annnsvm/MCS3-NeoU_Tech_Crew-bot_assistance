from classes.notebook.Notebook import Notebook
from helpers.decorators import note_input_error

class TagCommands:

    @note_input_error
    def add_tag(args, book: Notebook):
        note_name, tags = args
        note = book.find(note_name)
        if note:
            note.add_tag(tags)
            return "New tags added"
        else:
            return "There is no note with that name."

    @note_input_error
    def remove_tag(args, book: Notebook):
        name, tag = args
        if not book.find(name):
            return "Tag not found."
        else:
            note = book.find(name)
            note.remove_old_tag(tag)
            return "Tag removed."