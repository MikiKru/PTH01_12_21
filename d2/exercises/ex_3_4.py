def my_factorial(n):
    """
    Function returns factorial of given number n

    :param n: natural number
    :return: factorial of n
    """
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

n = 49
k = 6
win_probability = my_factorial(n)/(my_factorial(k) * my_factorial(n - k))
print(win_probability)
print(f"Prawdopodobieństwo wyganej: {1/win_probability:.10f}")