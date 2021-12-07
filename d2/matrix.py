matrix = [[1,2,3],[2,3,4],[3,4,5]]

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()

print(matrix[2][1])

print([col for row in matrix for col in row if col % 2 == 0])