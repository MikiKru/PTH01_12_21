def get_even(digit):
    return digit % 2 == 0 and digit != 0
def dec_to_bin(digit):
    return bin(digit)
def sorting_by_name_and_gender(name):
    if name[-1] == 'a':
        return 0, name
    else:
        return 1, name

digits = range(10)
after_filtering = list(filter(get_even, digits))
print(after_filtering, *after_filtering)
numbers = [2,3,4,2]
after_filtering_mapping = map(dec_to_bin, after_filtering)
print(*after_filtering_mapping)

example = [2,2,4,3,6,7,5,7,5,3,4]
names = ["Michał","Ala","Ela","Jan","Adam","Ada"]
print(sorted(example))
print(sorted(names, reverse=True))
print(sorted(names, key=sorting_by_name_and_gender))


