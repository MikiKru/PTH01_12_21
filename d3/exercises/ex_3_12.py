# record = dict(zip(["name", "last_name", "address", "gender", "age"] , ["Jan", "Kowalski", "Warszawa", True, 25]))

record1 = {"name" : "Jan", "lastName" : "Kowalski", "address" : "Warszawa", "gender" : True, "age" : 25}
record2 = {'name': 'Dawid','lastName': 'Michalczyk','address': 'Warszawa', 'gender': True, 'age': 25}
record3 = {"name" : "Alicja", "lastName" : "Kot" , "address" : "Katowice" , "gender" : False, "age" : 38}
record4 = {"name" : "Anna", "lastName": "Nowak", "address": "Szczecin", "gender" : False, "age" : 37}
record5 = {"name" : "Maciej", "lastName" : "Urbanski", "address" : "Łódź", "gender" : True, "age" : 44}

database_table = [record1, record2, record3, record4, record5]

# 1. SELECT * FROM table WHERE gender = True and address = 'Warszawa'

# 2. SELECT * FROM table WHERE age between 30 and 40

# 3. SELECT avg(age) FROM table WHERE name like 'A%'