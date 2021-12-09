from math import hypot

from d4.mvc.models import Point2D

class Point2D:
    def __init__(self, x, y):
        self.__set_x(x)
        self.__set_y(y)
    def __get_x(self):
        return self.__x
    def __get_y(self):
        return self.__y
    def __set_x(self, x):
        self.__x = x
    def __set_y(self, y):
        self.__y = y
    def __str__(self):
        return f"x={self.__get_x()} y={self.__get_y()}"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ge__(self, other):
        return hypot(self.x, self.y) >= hypot(other.x, other.y)
    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)

p1 = Point2D(1,2)
p2 = Point2D(3,3)
p3 = Point2D(3,3)
print(p1 == p2)
print(p3 == p2)
print(p1 >= p2)
print(p3 >= p2)

