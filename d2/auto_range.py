temps = range(-20, 21)
for num in temps:
    if not num:
        print(num, end=" ")
        continue
    print(f"{num:+}", end=" ")
print()
print(*temps)

