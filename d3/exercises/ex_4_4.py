import statistics


def get_data():
    record1 = {"name": "Jan", "lastName": "Kowalski", "address": "Warszawa", "gender": True, "age": 25}
    record2 = {'name': 'Dawid', 'lastName': 'Michalczyk', 'address': 'Warszawa', 'gender': True, 'age': 25}
    record3 = {"name": "Alicja", "lastName": "Kot", "address": "Katowice", "gender": False, "age": 38}
    record4 = {"name": "Anna", "lastName": "Nowak", "address": "Szczecin", "gender": False, "age": 37}
    record5 = {"name": "Maciej", "lastName": "Urbanski", "address": "Łódź", "gender": True, "age": 44}
    return [record1, record2, record3, record4, record5]

f1 = lambda data, gender=True, address='Warszawa' : [record for record in data if record["gender"] == gender and record["address"] == address]
f2 = lambda data, low_tresh, high_tresh: [record for record in data if record["age"] >= low_tresh and record["age"] <= high_tresh]
f3 = lambda data, gender, name_starts_with='A' : \
    statistics.mean([record["age"] for record in data if record["name"][0] == name_starts_with and record["gender"] == gender]) \
        if [record["age"] for record in data if record["name"][0] == name_starts_with and record["gender"] == gender] else 0


print(f1(get_data()))
print(f2(get_data(), 30, 40))
print(f3(get_data(),False))