from d5.exercises.ex_6_1.model.address import Address
from d5.exercises.ex_6_1.model.person import Person

a1 = Address("Królewska", "00-232", "Warszawa")
p1 = Person("Adam", "Kowalski", a1)
p2 = Person("Anna", "Kowalska", a1)

print(p1)
print(p2)