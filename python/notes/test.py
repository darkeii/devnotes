row = 3
column = 3

matrix = [[0] * column for _ in range(row)]

matrix[2][1] = 9

for i in matrix:
    print(i, end="\n")



