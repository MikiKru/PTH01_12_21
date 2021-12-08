from d3.functions.functions import *

hello_world()
hello_me("Michał")

print(get_random_value())
print(division(b=3, a=2))
print(division(3, 2))
print(division(3,0))

print(filter_by_treshold([2,1,3,2,4,5,4,3], 3))
print(len(filter_by_treshold([2,1,3,2,4,5,4,3], 3)))

print(filter_by_treshold([.2,.1,.3,.2,.4,.5,.4,.3], get_random_value()))

# wywołania funkcji z parametrami domyślnymi
print(get_record("Adam", "Kowalski", age=30))
print(get_record("Anna", "Kowalska", age=29, gender=False))

# Parametry nienazwane - dowolna ilość
print("Średnia ocen:",get_avg_from_grades(3,4.5,3,5,4))
print("Średnia ocen:",get_avg_from_grades(3,5,4))

# Parametry nazwane - dowolna ilość
print("Średnia ocen:",get_avg_from_grades_named_params(grade1=3,grade2=5,grade3=4))
print("Średnia ocen:",get_avg_from_grades_named_params(grade1=3.5,grade2=5))


