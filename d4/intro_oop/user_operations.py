class User:
    user_id = 1
    def __init__(self, name : str, last_name : str, age : int, gender : bool, address : str):               # konstruktor klasy - incjalizacja pól klasowych nowo utworzonego obiektu
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
    def __str__(self):                                      # tekstowa reprezentacja obiektu
        return f"{self.name} {self.last_name} {self.age} {self.gender} {self.address}"
    def increment_user_id(self):
        self.user_id += 1       # utworzenie zmiennej globalnej w klasie
    def set_user_id(self, user_id):     # modyfikacja
        self.user_id = user_id
    def get_user_id(self):              # pobierania
        return self.user_id

user1 = User("Adam", "Kowalski", 25, True, "Warszawa")
user2 = User("Ada", "Nowak", 25, False, "Warszawa")
user1.age = 28
setattr(user1, "name", "Jan")
print(getattr(user2, "name"))
# print(user1.name, user1.last_name, user1.gender, user1.age, user1.address)
print(user1)
print(user2.__str__())


#
# # statyczne odwołania do atrybutów klasy
# print(User.__name__)
# print(User.__dict__)
# print(User.__module__)
# print(User.__bases__)
# print(User.__doc__)
# # utworzenie obiektu = instancja klasy
# user1 = User()      # utworzenie nowego obiektu - uzyskanie dostępu do wszystkich pól i metod klasy
# user1.increment_user_id()
# user1.increment_user_id()
# user1.increment_user_id()
# print(user1.user_id)
# user2 = User()
# user2.increment_user_id()
# print(user1.user_id, user2.user_id)
# user3 = user1       # utworzenie na podstawie obiektu istniejącego
# user3.increment_user_id()
# print(user1.user_id, user2.user_id, user3.user_id)
# user2.set_user_id(0)
# print(user1.get_user_id(), user2.get_user_id(), user3.get_user_id())
#

