def addition(number1: float, number2: float) -> float:
    """
    Function for addition two numbers

    ...
    ...
    ...
    :param number1: first element
    :param number2: second element
    :return: sum of number1 and number2
    :exception: raise ecxeption type ...
    """
    result: float
    result = number1 + number2
    return result


print(addition.__doc__)
print(addition(1, 3.))
# print(addition("1", 3.))
