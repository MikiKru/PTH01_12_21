class MathOperations:
    def __init__(self, num1 : float, num2 : float):
        self.__set_num1(num1)
        self.__set_num2(num2)
    def __get_num1(self):
        print("jestem w getterze num 1")
        return  self.__num1
    def __get_num2(self):
        return self.__num2
    def __set_num1(self, num1):
        print("jestem w setterze num 1")
        self.__num1 = abs(num1)
    def __set_num2(self, num2):
        self.__num2 = abs(num2)
    num1 = property(__get_num1, __set_num1)
    num2 = property(__get_num2, __set_num2)


m = MathOperations(1,3)
print(m.num1, m.num2)
m.num1 = 10
m.num2 = 15
print(m.num1, m.num2)

