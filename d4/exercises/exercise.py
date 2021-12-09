# napisz funkcję x^y, x,y - integer +
# x^3 = x*x*x

def power(x : int,y : int) -> int:
    result: int = 1
    for _ in range(y):
        result *= x
    return result

print(power(2,3))
print(power(0,3))
print(power(3,0))
