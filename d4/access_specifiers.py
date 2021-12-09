class Example:
    def __init__(self, normal, private, strong_private):
        self.normal = normal
        self._private = private
        self.__strong_private = strong_private
    def get_strong_private(self):
        return self.__strong_private
    def set_strong_private(self, value):
        self.__strong_private = value

e = Example(1,2,3)
print(e.normal)
print(e._private)
# print(e.__strong_private)
print(e.__dict__)
print(e._Example__strong_private)
e.set_strong_private(555)
print(e.get_strong_private())