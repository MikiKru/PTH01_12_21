year = int(input("podaj rok"))
day = 13

friday_13_counter = 0
friday_13_months = ""
for month in range(1, 13):
    z = year - 1 if month < 3 else year
    c = 0 if month < 3 else 2
    day_week_index = (int(23 * month / 9) + 13 + 4 + year + int(z / 4) - int(z / 100) + int(z / 400) - c) % 7

    if day_week_index == 5:
        friday_13_counter += 1
        friday_13_months += f"{month:02} "


print(f"Ile było piątków 13 w roku {year}? {friday_13_counter}")
print(friday_13_months.split())