roman_arabic_conv = { "I" : 1, "II" : 2, "III" : 3 , "IV" : 4, "V" : 5}

# wstawianie nowej wartości do słownika
# 1
roman_arabic_conv.update(VI=6, VII=7)
# 2
roman_arabic_conv["VIII"] = 8
roman_arabic_conv["IX"] = 10
# modyfikacja
roman_arabic_conv["IX"] = 9
roman_arabic_conv["X"] = 10
# usuwanie
roman_arabic_conv.pop("X")

print(roman_arabic_conv)
print(roman_arabic_conv.items())
print(roman_arabic_conv.keys())
print(roman_arabic_conv.values())

for key, value in roman_arabic_conv.items():
    print(key, value)

arabic_to_roman_conv = {value : key for key, value in roman_arabic_conv.items()}
print(arabic_to_roman_conv)
print(roman_arabic_conv)

# pobieranie wartości po kluczu
print(arabic_to_roman_conv.get(3), arabic_to_roman_conv.get(7))
print(roman_arabic_conv.get("III"), roman_arabic_conv.get("VII"))

# ???
example = {1 : "A", 2: "A", 3: "B", 4: "C", 5 : "A"}
print({value : key for key, value in example.items()})
