n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_result = 0
for i in range(n):
    for j in range(n-2):
        result = (matrix[i][j] + matrix[i][j+1] + matrix[i][j+2])
        if max_result < result:
            max_result = result

print(max_result)