def day_index(year, month, day):
    z = year - 1 if month < 3 else year
    c = 0 if month < 3 else 2
    return (int(23 * month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7

def day_name(day_index):
    return ('niedziela','poniedziałek','wtorek','środa',"czwartek",'piątek','sobota')[day_index]

def get_day_name(date, sep='-'):            # format wprowadzania daty YYYY-MM-dd
    print(str(date).split(sep))
    year, month, day = str(date).split(sep)
    return int(year), int(month), int(day)

year, month, day = get_day_name(input("podaj datę w formacie YYYY-MM-dd"))
print(day_name(day_index(year, month, day)))
