from math import factorial

n = 49
k = 6

win_probability = factorial(n) / (factorial(k) * factorial(n-k))

print(f"Szanse na rozbicie banku: {1 / win_probability:.10f}")