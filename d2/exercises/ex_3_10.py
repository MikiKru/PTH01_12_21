size = int(input("input the matrix size: \n"))

print([[1 if row == col else 0 for col in range(size)] for row in range(size)])
