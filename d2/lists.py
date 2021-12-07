names = ['Adam','Ewa', 'Ala']

print(names)
print(names[0])
# modyfikacja
names[1] = 'Ola'
print(names, names[0], names[1], names[2])
# usuwanie
names.remove('Ola')
print(names, names[0], names[1])
# wprowadzenie nowych elementów
names.append("Jan")
print(names)
names.insert(1, "Ela")
print(names)
print(f"usunięto: {names.pop()}", names)
# edycja w miejscu - mutowalność
print(names)
names.reverse()     # wykonuje opearacje na mutowalnym obiekcie
print(names)