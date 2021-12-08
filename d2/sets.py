s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

print("suma", s1 | s2)
print("część wspólna", s1 & s2)
print("różnica", s1 - s2)
print("różnica", s2 - s1)
print("różnica symetryczna", s2 ^ s1)

user_priviliges = {'user', 'admin'}

print('moderator' in user_priviliges)
print('user' in user_priviliges)

print(list(user_priviliges)[0])

