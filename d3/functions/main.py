from d3.functions.functions import hello_world, hello_me, get_random_value, division, filter_by_treshold, get_record

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


