n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

def if_range(r, c, n, m):
    return 0 <= r and 0 <= c and r < n and c < m 

def checking(r, c):
    result = 0
    if if_range(r-2, c, n, m) and if_range(r-1, c, n, m) and matrix[r-2][c] == matrix[r-1][c] == 'E':
        result += 1 
    if if_range(r+2, c, n, m) and if_range(r+1, c, n, m) and matrix[r+2][c] == matrix[r+1][c] == 'E':
        result += 1
    if if_range(r, c+2, n, m) and if_range(r, c+1, n, m) and matrix[r][c+2] == matrix[r][c+1] == 'E':
        result += 1
    if if_range(r, c-2, n, m) and if_range(r, c-1, n, m) and matrix[r][c-2] == matrix[r][c-1] == 'E':
        result += 1
    if if_range(r-2, c-2, n, m) and if_range(r-1, c-1, n, m) and matrix[r-2][c-2] == matrix[r-1][c-1] == 'E':
        result += 1
    if if_range(r-2, c+2, n, m) and if_range(r-1, c+1, n, m) and matrix[r-2][c+2] == matrix[r-1][c+1] == 'E':
        result += 1
    if if_range(r+2, c-2, n, m) and if_range(r+1, c-1, n, m) and matrix[r+2][c-2] == matrix[r+1][c-1] == 'E':
        result += 1
    if if_range(r+2, c+2, n, m) and if_range(r+1, c+1, n, m) and matrix[r+2][c+2] == matrix[r+1][c+1] == 'E':
        result += 1
    return result

result = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            result += checking(i, j)

print(result)