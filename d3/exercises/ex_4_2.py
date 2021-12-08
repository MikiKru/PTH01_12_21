import statistics

def get_data():
    record1 = {"name": "Jan", "lastName": "Kowalski", "address": "Warszawa", "gender": True, "age": 25}
    record2 = {'name': 'Dawid', 'lastName': 'Michalczyk', 'address': 'Warszawa', 'gender': True, 'age': 25}
    record3 = {"name": "Alicja", "lastName": "Kot", "address": "Katowice", "gender": False, "age": 38}
    record4 = {"name": "Anna", "lastName": "Nowak", "address": "Szczecin", "gender": False, "age": 37}
    record5 = {"name": "Maciej", "lastName": "Urbanski", "address": "Łódź", "gender": True, "age": 44}
    return [record1, record2, record3, record4, record5]
def get_data_by_gender_and_address(data, gender=True, address='Warszawa'):
    return [record for record in data if record["gender"] == gender and record["address"] == address]
def get_data_by_age(data, low_tresh, high_tresh):
    return [record for record in data if record["age"] >= low_tresh and record["age"] <= high_tresh]
def get_mean_age(data, gender, name_starts_with='A'):
    result = [record["age"] for record in data if record["name"][0] == name_starts_with and record["gender"] == gender]
    return statistics.mean(result) if result else 0

print(get_data_by_gender_and_address(get_data()))
print(get_data_by_age(get_data(), 20, 40))
print(get_mean_age(get_data(),True))