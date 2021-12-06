year = 2019

isLeapYear = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(f"Rok {year} - jest przestępny? {isLeapYear}")