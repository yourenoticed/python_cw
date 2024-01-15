from note.note import Note
from datetime import datetime

class Notebook_Parser():
    def __init__(self, notes: list[dict]):
        self.notes = notes
    
    def parse_note(self, note: dict) -> Note:
        if ("id" in note) and ("title" in note) and ("note" in note) and ("creation_date" in note) and ("last_edit_date" in note):
            creation_date = datetime.fromisoformat(note["creation_date"])
            last_edit_date = datetime.fromisoformat(note["last_edit_date"])
            return Note(note["id"], note["title"], note["note"], creation_date, last_edit_date)
        raise Exception("Wrong note format")
    
    def parse_notes(self) -> list[Note]:
        note_list = list()
        for note in self.notes:
            note_list.append(self.parse_note(note))
        return note_list