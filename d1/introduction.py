# CTRL + / - autokomentarz
# CTRL + d - duplikowanie linii na której znajduje się kursor
# CTRL + q - auto-dokumentacja


if_one = 5

if True:
    print(True)
    print(True)
    print(True)
print("Poza if-em")
print("Michał", 2 + 5, True, sep=";", end='.')  # domyślnie sep=' ' i end='\n'
print("XXX")

# name = input("Podaj imię: ")                    # zwraca typ string
# number = int(input("Podaj liczbę: "))
# print("Twoje imię: " + name, "Twoja liczba: " + str(number))
# print(f"Twoje imię: {name} Twoja liczba: {number}")
#
# print("poza komentarzem")

x = 1
y = x
print(x, y)
x = 2
y = x
print(x, y)
# del(y)                                            # usuwanie obiektu z pamięci
print(x, y)



