from classes.notebook.Notebook import Notebook

class TextCommands:
    def replace_note_text(args, book: Notebook):
        note_name = args[0]
        note_text = args[1]
        note = book.find(note_name)
        if note:
            note.add_note(note_text)
            return "Note text replaced"
        else:
            return "Note not found"


    def add_note_text(args, book: Notebook):
        note_name = args[0]
        note_text = args[1]
        note = book.find(note_name)
        if note:
            note.add_text(note_text)
            return "Text added"
        else:
            return "Note not found"