from .note import Note

class Notebook():
    def __init__(self, notebook=None):
        if notebook is None:
            self.notebook = list()
        else:
            self.notebook = notebook
    
    def add_note(self, note: Note) -> None:
        self.notebook.append(note)
    
    def remove_note(self, note: Note) -> bool:
        if note in self.notebook:
            self.notebook.remove(note)
            return True
        return False
        
    def edit_note(self, note: Note, new_title=None, new_note=None) -> bool:
        return note.edit_note(new_title, new_note)
    
    def get_note_by_id(self, id: int) -> Note | None:
        for note in self.notebook:
            if note.id == id:
                return note
        return None
    
    def get_notes_by_title(self, prompt: str) -> list[Note]:
        result = list()
        for note in self.notebook:
            if prompt in note.title:
                result.append(note)
        return result
    
    def get_notes_data(self) -> list[dict]:
        return [note.get_data() for note in self.notebook]
    
    def get_notes_str(self) -> list[str]:
        return [note.__str__() for note in self.notebook]
        
    def __iter__(self):
        return self.notebook.__iter__()