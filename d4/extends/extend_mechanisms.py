class Trainer:
    def __init__(self, trainer_name):
        self.trainer_name = trainer_name
    def get_name(self):
        return self.trainer_name
class Software(Trainer):
    def __init__(self, technology, version, price):
        self.technology = technology
        self.version = version
        self.price = price
        print("Jestem w konstruktorze Software")
    def __str__(self):
        print("Str klasy Software")
        return f"{self.technology} {self.version} {self.price}"
class Course(Software):
    def __init__(self, name, term, technology, version, price):
        super().__init__(technology, version, price)        # wywołanie kontruktora klasy nadrzędnej !!! musi być na pierwszej linii
        self.name = name
        self.term = term
        print("Jestem w konstruktorze Course")
    def __str__(self):
        print("Str klasy Course")
        return f"{self.name} {self.term} {super().__str__()} {super().get_name()}"

# s = Software("MS Windows", "11", 1500)      # dsotęp do pól i metod klasy Software i object
c = Course("PYTH01", "06-01.12.2021", "Python", "Dzienna", 2000)
c.trainer_name = "MK"
print(c.__str__())

print(Course.__bases__, Software.__bases__, Trainer.__bases__, object.__bases__)
print(Course.__mro__)

