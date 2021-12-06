value = 0

if value == 0:
    print('Zero')
elif value > 0 and value % 2 == 0:
    print('liczba dodatnia parzysta')
elif value > 0 and value % 2 != 0:
    print('liczba dodatnia nieparzysta')
elif value < 0 and value % 2 == 0:
    print('liczba ujemna parzysta')
else:
    print('liczba ujemna nieparzysta')