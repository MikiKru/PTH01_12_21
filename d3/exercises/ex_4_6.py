def day_index(year : int, month : int, day : int) -> int:
    z = year - 1 if month < 3 else year
    c = 0 if month < 3 else 2
    return (int(23 * month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7

def day_name(day_index : int) -> str:
    return ('niedziela','poniedziałek','wtorek','środa',"czwartek",'piątek','sobota')[day_index]

def get_day_name(date : str, sep : str ='-') -> tuple:
    print(str(date).split(sep))
    year, month, day = str(date).split(sep)
    return int(year), int(month), int(day)

#test
year, month, day = get_day_name("2020-03-03")
print(day_index(year, month, day))
print(day_name(1))

