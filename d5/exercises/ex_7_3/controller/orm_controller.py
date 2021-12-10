from d5.exercises.ex_7_3.model.address import Address
from d5.exercises.ex_7_3.model.person import Person


class ORM:
    def object_to_file(self, people):
        pass
    def file_to_object(self, path):
        pass


if __name__ == '__main__':
    a1 = Address("Królewska", "00-232", "Warszawa")
    p1 = Person("Adam", "Kowalski", a1)
    p2 = Person("Anna", "Kowalska", a1)
    people = [p1, p2]