from datetime import datetime

class Note():
    def __init__(self, id: int, title: str, note: str, creation_date=None, last_edit_date=None):
        self.id = id
        self.title = title
        self.note = note
        if creation_date is None:
            self.creation_date = datetime.now()
        else:
            self.creation_date = creation_date
        if last_edit_date is None:
            self.last_edit_date = self.creation_date
        else:
            self.last_edit_date = last_edit_date
        
    def edit_note(self, new_title=None, new_note=None) -> bool:
        if new_title is None and new_note is None:
            return False
        if new_title is not None:
            self.title = new_title
        if new_note is not None:
            self.note = new_note
        self.last_edit_date = datetime.now()
        return True
    
    def get_data(self) -> dict:
        data = {"id": self.id,
                "title": self.title,
                "note": self.note,
                "creation_date": self.creation_date.isoformat(),
                "last_edit_date": self.last_edit_date.isoformat()}
        return data
    
    def __str__(self):
        return f"title: {self.title}\nnote: {self.note}\ncreation date: {self._format_date(self.creation_date)}\nlast edited: {self._format_date(self.last_edit_date)}"
    
    def __rerp__(self):
        return self.get_data()
    
    def _format_date(self, date: datetime):
        formatted = f"{date.day}.{date.month}.{date.year} {date.hour}:{date.minute}:{date.second}"
        return formatted