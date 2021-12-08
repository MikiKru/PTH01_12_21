# record = dict(zip(["name", "last_name", "address", "gender", "age"] , ["Jan", "Kowalski", "Warszawa", True, 25]))
import statistics

record1 = {"name" : "Jan", "lastName" : "Kowalski", "address" : "Warszawa", "gender" : True, "age" : 25}
record2 = {'name': 'Dawid','lastName': 'Michalczyk','address': 'Warszawa', 'gender': True, 'age': 25}
record3 = {"name" : "Alicja", "lastName" : "Kot" , "address" : "Katowice" , "gender" : False, "age" : 38}
record4 = {"name" : "Anna", "lastName": "Nowak", "address": "Szczecin", "gender" : False, "age" : 37}
record5 = {"name" : "Maciej", "lastName" : "Urbanski", "address" : "Łódź", "gender" : True, "age" : 44}

database_table = [record1, record2, record3, record4, record5]

# 1. SELECT * FROM table WHERE gender = True and address = 'Warszawa'
men_in_warsaw = [record for record in database_table if record["gender"] and record["address"] == 'Warszawa']
print(men_in_warsaw)

# 2. SELECT * FROM table WHERE age between 30 and 40
people_with_age = [record for record in database_table if record["age"] >= 30 and record["age"] <= 40]
print(people_with_age)

# 3. SELECT avg(age) FROM table WHERE name like 'A%' and gender = False
ages = [record["age"] for record in database_table if record["name"][0] == "A" and not record["gender"]]
print("Średnia wieku",statistics.mean(ages))
