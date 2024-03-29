from service.service import Service
from notebook.note import Note

class Console_UI():
    def __init__(self):
        self.run()
            
    def run(self):
        self.notebook_init()
        if self.service is not None:
            self.main()
        else:
            print("Can't initialize notebook.")
    
    def main(self):
        running = True
        while running:
            choice = input("Menu:\n1. Print notes\n2. Add note\n3. Find notes\n4. Find a note\n5. Edit note\n6. Delete note\n7. Quit\n")
            match choice:
                case "1":
                    self.print_notes()
                case "2":
                    self.add_note()
                case "3":
                    notes = self.find_notes()
                    if notes:
                        for i, note in enumerate(notes):
                            print(i + 1, note)
                case "4":
                    print(self.find_note())
                case "5":
                    self.edit_note()
                case "6":
                    self.delete_note()
                case "7":
                    self.quit()
                    running = False
                case _:
                    print("Wrong option")    
        
    def print_notes(self):
        print("\nPrinting notes")
        for note in self.service.notebook:
            print(note)
            print()
        
    def add_note(self):
        print("\nAdding note")
        title = input("Enter note title: ")
        note = input("Enter note: ")
        self.service.add_note(title, note)
    
    def delete_note(self):
        print("\nDeleting note")
        note = self.find_note()
        if note is not None:
            self.service.remove_note(note)
            print("The note was removed successfully")
        print("Nothing was removed")
    
    def quit(self):
        self.service.save()
        
    def find_note(self) -> Note | None:
        notes = self.find_notes()
        if notes:
            if len(notes) == 1:
                print(f"Note found: {notes[0]}")
                return notes[0]
            searching = True
            while searching:
                for i, note in enumerate(notes):
                    print(f"{i + 1}. {note}")
                choice = input("What note are you looking for?\n")
                if choice.isdigit():
                    choice = int(choice)
                    if choice > 0 and choice <= len(notes):
                        return notes[choice - 1]
                    else:
                        print("Wrong option")
                else:
                    print("Your input wasn't a number. The search is stopped.")
                    return None
        print("No notes were found.")
        return None
    
    def find_notes(self) -> list[Note] | None:
        choice = input("What do you want to search by?\n1. Title\n2. Date\n")
        match choice:
            case "1":
                return self.find_notes_by_title()
            case "2":
                return self.find_notes_by_date()
            case _:
                return None
    
    def find_notes_by_title(self) -> list[Note]:
        prompt = input("Enter search prompt: ")
        return self.service.get_notes_by_title(prompt)
    
    def find_notes_by_date(self) -> list[Note] | None:
        start = input("Enter starting date (DD.MM.YYYY): ")
        if not self.service.is_date_valid(start):
            print("Not valid date")
        finish = input("Enter end date (DD.MM.YYYY): ")
        if finish == "":
            finish = None
        elif not self.service.is_date_valid(finish):
            print("Not valid date")
        return self.service.filter_by_date(start, finish)
        
    def edit_note(self):
        note = self.find_note()
        if note is not None:
            editing = True
            while editing:
                print(note)
                choice = input("What do you want to change?\n1. Title\n2. Note\n3. Quit\n").lower()
                if choice in ["1", "title"]:
                    print(note.title)
                    new_title = input(note.title +  " -> ")
                    self.service.edit_note(note, new_title=new_title)
                elif choice in ["2", "note"]:
                    new_note = input(note.note + " -> ")
                    self.service.edit_note(note, new_note=new_note)
                elif choice in ["3", "quit"]:
                    print("Finished editing")
                    editing = False
                else:
                    print("Wrong choice")
    
    def notebook_init(self):
        choice = input("Welcome to The Notebook.\nChoose an option to continue.\n1. Load exisitng notebook\n2. Create new notebook\n")
        match choice:
            case "1":
                self.file_init(False)
            case "2":
                self.file_init(True)
            case _:
                raise Exception("Wrong option")

    def file_init(self, new: bool):
        path = input("Enter path to the file: ")
        self.service = Service(path, new)
        
if __name__ == "__main__":
    ui = Console_UI()