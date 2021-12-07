text = "kajak...  :"
# czyszczenie danych
clean_text = [t.upper() for t in text if t.isalpha()]

# decyzja - palindrom?
# 1
clean_text2 = clean_text[: : -1]
print(clean_text == clean_text2)
# 2
print(clean_text[ : len(clean_text)//2] == clean_text[ : len(clean_text)//2 : -1])

