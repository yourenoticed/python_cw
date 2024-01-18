from datetime import datetime

class Date_Parser():
    def __init__(self):
        self.MAX_DAYS = {
            1: 31,
            2: 29,
            3: 31,
            4: 30, 
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        
    # Takes string of format DD.MM.YYYY and parses it to datetime
    def parse_date(self, date: str) -> datetime:
        date_l = date.split(".")
        validation = self._validate_date(date_l)
        if validation:
            date_l.reverse()
            return datetime.fromisoformat("-".join(date_l))
        raise Exception("Wrong date format")
    
    # All the methods below take list of strings of a format [DD, MM, YYYY]
    def _validate_date(self, date: list[str]) -> bool:
        if len(date) == 3 and self._are_digits(date):
            if self._valid_date(date):
                return True
        return False
    
    def _valid_date(self, date: list[str]) -> bool:
        date_int = [int(n) for n in date]
        d = date_int[0]
        m = date_int[1]
        y = date_int[2]
        if m > 0 and m <= 12:
            if d > 0 and d <= self.MAX_DAYS[m]:
                if m == 2 and d == 29 and not self._is_leap_year(y):
                    return False
                return True
        return False
            
    def _are_digits(self, arr: list[str]) -> bool:
        for n in arr:
            if not n.isdigit():
                return False
        return True
    
    def _is_leap_year(self, year: int):
        if year % 4 == 0:
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            return True
        return False