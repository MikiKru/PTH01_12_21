n = 1000
number = 1
while n > 0:
    if number % 2 == 0:
        print(number, end=" ")
        n -= 1      # n = n - 1
    number += 1
else:
    print("Po ostatniej iteracji")

