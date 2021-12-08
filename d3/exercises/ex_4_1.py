day = int(input("podaj dzień"))
month = int(input("podaj miesiąc"))
year = int(input("podaj rok"))

z = year - 1 if month < 3 else year
c = 0 if month < 3 else 2
day_of_week_index = (int(23 * month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7

day_index_mapper = ('niedziela','poniedziałek','wtorek','środa',"czwartek",'piątek','sobota')
print(f"Data: {day:02}.{month:02}.{year} - dzień tygodnia - {day_index_mapper[day_of_week_index]}")

def day_index(date):
    pass
def day_name(day_index):
    pass
def get_day_name(date, sep='-'):            # format wprowadzania daty YYYY-MM-dd
    pass
