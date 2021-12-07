months = ["styczeń","luty","marzec","kwiecień","maj","czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
quarter_length = 3

quarters = [[month for index, month in enumerate(months) if index // quarter_length == quarter] for quarter in range(4)]
print(quarters)


quarters2 = []
for quarter in range(4):
    quart = []
    for index, month in enumerate(months):
        if index // quarter_length == quarter:
            quart.append(month)
    quarters2.append(quart)
print(quarters2)