height = float(input("podaj wzrost [m]: "))
weight = int(input("podaj wagę [kg]: "))

bmi = weight/(height**2)

if bmi < 16 :
    diag="wygłodzony"
elif bmi < 17 :
    diag="wychudzony"
elif bmi < 18.5 :
    diag="niedowaga"
elif bmi < 25 :
    diag="wartość prawidłowa"
elif bmi < 30 :
    diag="nadwaga"
elif bmi < 35 :
    diag="I stopień otyłości"
elif bmi < 40 :
    diag="I stopień otyłości"
else:
    diag="I stopień otyłości"

weight_min = 18.5 * (height ** 2)
weight_max = 24.99 * (height ** 2)

print(f"Twój BMI to {bmi:.2f} - {diag}")
print(f"Prawidłowa waga dla Twojego wzrostu {weight_min:.1f} - {weight_max:.1f}")