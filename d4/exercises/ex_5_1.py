from datetime import date


class Person:
    def __init__(self, name: str, last_name: str, gender: bool, birth_year: int):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        if date.today().year < birth_year:
            self.birth_year = None
        else:
            self.birth_year = birth_year
    def how_many_years(self):
        return date.today().year - self.birth_year if self.birth_year != None else 'B/D'
    def __str__(self):
        return f"{self.name} {self.last_name}, płeć: {'M' if self.gender else 'K'}, wiek: {self.how_many_years()} lat"

p1 = Person("Adam","Nowak",True, 2022)
# p1.birth_year = p1.birth_year + 1
print(p1)

