from datetime import datetime
from notebook.notebook_parser import Notebook_Parser
from notebook.notebook import Notebook
from notebook.note import Note
from .filehandler import Filehandler
from .date_parser import Date_Parser
import json

class Service():
    def __init__(self, path: str, new_file: bool):
        self.path = path
        self.date_parser = Date_Parser()
        self.handler = Filehandler(path)
        if new_file:
            self.notebook = Notebook()
            self.id = 0
        else:
            self.notebook = Notebook(Notebook_Parser(json.loads(self.handler.read_file())).parse_notes())
            self.id = self.notebook.notebook[-1].id
        
    def save(self) -> None:
        data = self.notebook.get_notes_data()
        self.handler.write_to_file(json.dumps(data))
    
    def add_note(self, title: str, note: str) -> None:
        self.id += 1
        self.notebook.add_note(Note(self.id, title, note))
        
    def edit_note(self, note: Note, new_title=None, new_note=None) -> bool:
        return self.notebook.edit_note(note, new_title, new_note)
    
    def remove_note(self, note: Note) -> bool:
        return self.notebook.remove_note(note)
    
    def get_by_id(self, id: int) -> Note | None:
        return self.notebook.get_note_by_id(id)
    
    def get_notes_by_title(self, prompt: str) -> list[Note]:
        return self.notebook.get_notes_by_title(prompt)
    
    def get_notes_str(self):
        return self.notebook.get_notes_str()
    
    def filter_by_date(self, start: str, finish=None) -> list[Note] | None:
        try:
            start_date = self.date_parser.parse_date(start)
            if finish:
                finish_date = self.date_parser.parse_date(finish)
            else:
                finish_date = datetime.now()
            return self.notebook.filter_by_date(start_date, finish_date)
        except:
            return None
        
    def is_date_valid(self, date: str) -> bool:
        return self.date_parser._validate_date(date.split("."))