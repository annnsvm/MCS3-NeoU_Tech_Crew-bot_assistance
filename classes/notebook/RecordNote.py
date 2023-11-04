from classes.notebook.Note import Note
from classes.notebook.Name import Name
from classes.notebook.Tag import Tag


class RecordNote:
    def __init__(self, name):
        self.note_name = Name(name)
        self.tags = []
        self.note_text = None

    def add_tag(self, tag):
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
        self.note_text.value += f" {new_text}"
        return "The text has been updated"

    def __str__(self):
        return f"Note name: {self.note_name.value},\
        tags: {'; '.join(t.value for t in self.tags)}, \
        Note: {self.note_text.value if self.note_text else 'No notes'}"
