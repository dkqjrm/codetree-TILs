n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

tmp_total = 0
for i in matrix:
    tmp_total += sum(i)
    
for row in range(n):
    tmp_column_total = 0
    for column in range(n):
        tmp_column_total += matrix[row][column]
    matrix[row].append(tmp_column_total)


tmp = []
for column in range(n):
    tmp_row_total = 0
    for row in range(n):
        tmp_row_total += matrix[row][column]
    tmp.append(tmp_row_total)

matrix.append(tmp)


matrix[-1].append(tmp_total)

for i in matrix:
    print(*i)