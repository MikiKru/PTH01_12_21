elements = [2,3,1,4,3,4,5,6,32,2,234,5]
to_find = int(input("Jaką chcesz wyszukać liczbę? "))

for index, element in enumerate(elements):
    if element != to_find:
        continue                # przerwanie aktualnej iteracji i przejście do kolejnej
    print(f"Zanlezieono liczbę {to_find} na indeksie {index}")
    break                       # przerwanie pętli
else:
    print(f"Nie znaleziono liczby {to_find}")