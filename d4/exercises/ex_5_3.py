from datetime import date


class Person:
    def __init__(self, name: str, last_name: str, gender: bool, birth_year: int):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_gender(gender)
        self.set_birth_year(birth_year)
    def set_name(self, name : str):
        if name.isalnum():
            self.__name = name
        else:
            self.__name = 'anonim'
    def get_name(self):
        return self.__name
    def set_last_name(self, last_name : str):
        if last_name.isalnum():
            self.__last_name = last_name
        else:
            self.__last_name = 'anonim'
    def get_last_name(self):
        return self.__last_name
    def set_gender(self, gender : bool):
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_birth_year(self, birth_year : int):
        if date.today().year < birth_year or birth_year <= 0:
            self.__birth_year = None
        else:
            self.__birth_year = birth_year
    def get_birth_year(self):
        return self.__birth_year
    def how_many_years(self):
        return date.today().year - self.get_birth_year() if self.get_birth_year() != None else 'B/D'
    def output_format(self):
        return f"{self.get_name()}; {self.get_last_name()}; {self.get_gender()}; {self.get_birth_year()}"
    def __str__(self):
        return f"{self.get_name()} {self.get_last_name()}, płeć: {'M' if self.get_gender() else 'K'}, wiek: {self.how_many_years()} lat"
    name = property(get_name,set_name)
    last_name = property(get_last_name, set_last_name)
    gender = property(get_gender,set_gender)
    birth_year = property(get_birth_year, set_birth_year)

p = Person("Michał","Kru", True, 2000)
p.name = ""
p.birth_date = 2030
print(p)
print(p.output_format())