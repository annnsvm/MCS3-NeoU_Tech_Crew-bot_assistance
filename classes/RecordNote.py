from classes.Name import Name
from classes.Tag import Tag
from classes.Note import Note

class RecordNote:
    def __init__(self, name):
        self.note_name = Name(name)
        self.tags = []
        self.note_text = None
        
    def add_tag(self, tag):
        self.tags.append(Tag(tag))

    def remove_tag(self, tag_name):
        for i, tag in enumerate(self.tags):
            if tag.value == tag_name:
                del self.tags[i]
                return "Tag removed."
        raise ValueError("Tag not found.")

    def edit_note(self, old_note, new_note):
        return "Note changed."

    def find_tag(self, tag_name):
        for tag in self.tags:
            if tag.value == tag_name:
                return tag

    def add_note(self, note_text):
        self.note_text = Note(note_text)
        return "Note added"

    def __str__(self):
        return f"Note name: {self.note_name.value},\
        tags: {'; '.join(t.value for t in self.tags)}, \
        Note: {self.note_text.value if self.note_text else 'No notes'}"