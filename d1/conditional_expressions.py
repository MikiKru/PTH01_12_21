name = input("Podaj imię: ")

genderName = "KOBIETA" if name[len(name) - 1].upper() == 'A' else "MĘŻCZYZNA"
print(f"{name} to {genderName}")