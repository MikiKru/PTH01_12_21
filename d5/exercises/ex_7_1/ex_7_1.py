
with open(r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w1.txt', mode="r", encoding="utf-8") as file1:
    for line in file1:
        print(line.strip())     # strip wycina znaki przejścia do nowej lini z końca i początku tekstu

with open(r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w2.txt', mode="r", encoding="utf-8") as file2:
    for line in file2:
        print(line.strip())

# with open("../files/w2.txt", mode="r", encoding='utf-8') as file2:
#     for line in file2:
#         print(line.strip())

# wypisz linie naprzemian z obu plików
# file = open("w1.txt")
# #...
# file.close()

with open(r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w1.txt', mode="r", encoding='utf-8') as file1, \
        open(r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w2.txt', mode="r", encoding='utf-8') as file2:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
longer = file1_lines
smaller = file2_lines
if len(file1_lines) < len(file2_lines):
    longer = file2_lines
    smaller = file1_lines
for index, line in enumerate(longer):
    print(line.strip())
    if index < len(smaller):
        print(smaller[index].strip())
