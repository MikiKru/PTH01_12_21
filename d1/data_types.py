name = 'Michał'
integer_number = 1
integer_number1 = 1
float_number = 1.92
print(type(name), type(integer_number), type(float_number))
print(name.upper(), name.lower(), name + '2', name * 3)
print(integer_number * 5, str(integer_number) * 5)
print(int(float_number))                    # konwersja zawężająca
print(float(integer_number))                # konwersja rozszerzająca
print(hex(name.__hash__()))
print(hex(id(integer_number)))
print(hex(id(integer_number1)))
