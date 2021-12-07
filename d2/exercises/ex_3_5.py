import math

location = [0,0]
while True:
    move_direction = input("podaj kierunek i krok")
    if not move_direction:
        print("Obliczanie położenia", location)
        print(round(math.hypot(location[0], location[1]), 2))
        break
    direction = move_direction.split()[0]
    step = int(move_direction.split()[1])
    if direction.upper() == 'N':
        location[1] += step
    if direction.upper() == 'S':
        location[1] -= step
    if direction.upper() == 'W':
        location[0] -= step
    if direction.upper() == 'E':
        location[0] += step