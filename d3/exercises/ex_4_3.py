import statistics


def get_data():
    record1 = {"name": "Jan", "lastName": "Kowalski", "address": "Warszawa", "gender": True, "age": 25}
    record2 = {'name': 'Dawid', 'lastName': 'Michalczyk', 'address': 'Warszawa', 'gender': True, 'age': 25}
    record3 = {"name": "Alicja", "lastName": "Kot", "address": "Katowice", "gender": False, "age": 38}
    record4 = {"name": "Anna", "lastName": "Nowak", "address": "Szczecin", "gender": False, "age": 37}
    record5 = {"name": "Maciej", "lastName": "Urbanski", "address": "Łódź", "gender": True, "age": 44}
    return [record1, record2, record3, record4, record5]

gender = True
address = 'Warszawa'
low_tresh = 35
high_tresh = 40

def filter_get_data_by_gender_and_address(record):
    global gender, address
    return record["gender"] == gender and record["address"] == address
def get_data_by_age(record):
    global low_tresh, high_tresh
    return record["age"] >= low_tresh and record["age"] <= high_tresh
def get_female_A(record):
    return record["name"][0] == 'A' and not record['gender']
def get_age(record):
    return record['age']

print(*filter(filter_get_data_by_gender_and_address,get_data()))
print(*filter(get_data_by_age,get_data()))
femaleA = list(filter(get_female_A,get_data()))
ages = list(map(get_age, femaleA))
print(statistics.mean(ages))