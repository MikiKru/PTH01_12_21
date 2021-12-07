x = ['a', 'b', 'c', 'd', 'e']
print(x[1:4])

text = 'he ate camel food'
print(text[-1:2:-2])
print(text[-1:2:2])


year, month, day = (2020, 10, 20)
print(year)
print(month)
print(day)
year, _, day = (2021, 1, 1)
print(year)
print(day)
first, *middle, last = range(50)
print(first)
print(middle)
print(last)

# multiplikacja
numbers = range(5)
print(list(numbers) * 3)
print("ALA" * 3)
print(*numbers)
print(30 in numbers)

# błędy
# txt = "XYZ"
# print(txt[10])
# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

