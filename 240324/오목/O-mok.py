n = 19
matrix = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y, n):
    return 0 <= x and 0 <= y and x < n and y < n

def checking(x, y):
    now = matrix[i][j]
    if now == 1 or now == 2: # 검 or 흰
        if in_range(i-2, j, n) and in_range(i-1, j, n) and in_range(i, j, n) and in_range(i+1, j, n) and in_range(i+2, j, n) and matrix[i-2][j] == matrix[i-1][j] == matrix[i][j] == matrix[i+1][j] == matrix[i+2][j]:
            return now, i, j
        elif in_range(i, j-2, n) and in_range(i, j-1, n) and in_range(i, j, n) and in_range(i, j+1, n) and in_range(i, j+2, n) and matrix[i][j-2] == matrix[i][j-1] == matrix[i][j] == matrix[i][j+1] == matrix[i][j+2]:
            return now, i, j
        elif in_range(i-2, j-2, n) and in_range(i-1, j-1, n) and in_range(i, j, n) and in_range(i+1, j+1, n) and in_range(i+2, j+2, n) and matrix[i-2][j-2] == matrix[i-1][j-1] == matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2]:
            return now, i, j
        elif in_range(i-2, j+2, n) and in_range(i-1, j+1, n) and in_range(i, j, n) and in_range(i+1, j-1, n) and in_range(i+2, j-2, n) and matrix[i-2][j+2] == matrix[i-1][j+1] == matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2]:
            return now, i, j
        else:
            return 0
    else:
        return 0

        


for i in range(n):
    for j in range(n):
        result = checking(i, j)
        if result != 0:
            print(result[0])
            print(result[1] + 1, result[2] + 1)
            break
        else:
            print(result)