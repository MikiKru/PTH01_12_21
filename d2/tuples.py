from math import pi

params = (1.23, 3.21, 2.34, "TRESH_LOW", "TRESH_HIGH", pi, 1.23)
print(params)
for index, param in enumerate(params):
    print(index, param)

# params[0] = 3     - krotki są niezmienne
print(params.index(3.21))
print(params.count("DD"))
print(len(params))
print(params[0], params[len(params) - 1], params[-1])
print(params[0:5])          # od indeksu włącznie do indeksu wyłącznie
print(params[0:5:2])        # od indeksu włącznie do indeksu wyłącznie co drugi element
print(params[ : :2])        # od cała krotka co drugi element
print(params[-1], params[-2], params[-len(params)])     # indeksowanie wartościami ujemnymi

