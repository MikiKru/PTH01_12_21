import datetime

class YearException(Exception):
    def __init__(self):
        print("rok musi być większy od zera i mniejszy od aktualnego")
class MonthException(Exception):
    def __init__(self):
        print("miesiąc musi być w przedziale od 1 do 12")

while True:
    try:
        date = input("podaj datę YYYY-MM-dd")
        year, month, day = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        if year < 0 or year > datetime.date.today().year:
            raise YearException
        if month not in range(1,13):
            raise MonthException
        print(year, month, day)
    except ValueError as e:
        print("błędny format daty")
    except (YearException, MonthException):
        print("błędna walidacja")
    except Exception as e:

        print("inny błąd")
    else:
        print("jestem w else - ok i przerywam pętle")
        break
print("jestem za pętlą - ok")