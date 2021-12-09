from datetime import date

class Person:
    def __init__(self, name: str, last_name: str, gender: bool, birth_year: int):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        if date.today().year < birth_year or birth_year <= 0:
            self.birth_year = None
        else:
            self.birth_year = birth_year
    def how_many_years(self):
        return date.today().year - self.birth_year if self.birth_year != None else 'B/D'
    def __str__(self):
        return f"{self.name} {self.last_name}, płeć: {'M' if self.gender else 'K'}, wiek: {self.how_many_years()} lat"
    def __eq__(self, other):
        return self.name == other.name and self.last_name == other.last_name
    def __lt__(self, other):
        return self.last_name < other.last_name, self.name < other.name
    def __gt__(self, other):
        return self.how_many_years() > other.how_many_years(), self.last_name > other.last_name, self.name > other.name
p1 = Person("Adam","Nowak",True, 1999)
p2 = Person("Jan","Nowak",True, 1990)
p3 = Person("Roman","Kos",True, 1977)
p4 = Person("Adam","Nowak",True, 1997)
print(p1 == p4)
print(p1 < p2)
print(p1 > p2)
