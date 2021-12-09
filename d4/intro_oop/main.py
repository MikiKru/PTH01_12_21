from bs4 import BeautifulSoup
from d4.intro_oop.user_operations import User


def compare_objects(object):
    print(isinstance(object, User))

user1 = User()
bs = BeautifulSoup()
compare_objects(user1)
compare_objects(bs)