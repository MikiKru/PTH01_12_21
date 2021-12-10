from d5.exercises.ex_7_3.model.address import Address
from d5.exercises.ex_7_3.model.person import Person

# p = Person("Michał", "Kru", Address("X", "X","X"))
p = Person("Michał", "Kru", None)
# p = None
if __debug__:
    assert p.address != None, 'adres obiektu person nie może być None'

