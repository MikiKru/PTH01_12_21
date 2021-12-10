
with open(r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w1.txt', mode="r", encoding="utf-8") as file1:
    for line in file1:
        print(line.strip())     # strip wycina znaki przejścia do nowej lini z końca i początku tekstu

with open(r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w2.txt', mode="r", encoding="utf-8") as file2:
    for line in file2:
        print(line.strip())

with open("../files/w2.txt", mode="r", encoding='utf-8') as file2:
    for line in file2:
        print(line.strip())