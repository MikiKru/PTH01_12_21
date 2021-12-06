
while True:
    decision = input("Wybierz zadanie: \n(1) - zad1 \n(2) - zad2 \n(q) - wyjście")
    if decision == '1':
        print("Rozwiązanie zadania 1")
    elif decision == '2':
        print("Rozwiązanie zadania 2")
    elif decision.upper() == 'Q':
        print('Wyjście')
        break
    else:
        print("Błędny wybór")