
with open("w1.txt", mode="r", encoding="utf-8") as file1:
    for line in file1:
        print(line.strip())     # strip wycina znaki przejścia do nowej lini z końca i początku tekstu

with open("w2.txt", mode="r", encoding="utf-8") as file2:
    for line in file2:
        print(line.strip())

