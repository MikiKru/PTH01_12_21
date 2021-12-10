from d5.exercises.ex_7_3.model.address import Address
from d5.exercises.ex_7_3.model.person import Person


class ORM:
    def object_to_file(self, people, path):
        with open(path, "w", encoding="utf-8") as file:
            for person in people:
                file.write(f'{person.to_csv()}\n')
    def file_to_object(self, path):
        people = []
        with open(path, "r", encoding="utf-8") as file:
            for person in file:
                p = person.split("; ")
                people.append(Person(p[0], p[1], Address(p[2], p[3], p[4])))
        return people

if __name__ == '__main__':
    orm = ORM()
    a1 = Address("Królewska", "00-232", "Warszawa")
    a2 = Address("Kocia", "00-232", "Warszawa")
    p1 = Person("Adam", "Kowalski", a1)
    p2 = Person("Anna", "Kowalska", a1)
    p3 = Person("Jan", "Nowak", a2)
    people = [p1, p2, p3]
    orm.object_to_file(people, "people.csv")
    for p in orm.file_to_object("people.csv"):
        print(p, end="")