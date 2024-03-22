n = int(input())

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y, n):
    return 0 <= x and x <= n-1 and 0 <= y and y <= n-1

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

result = 0

for i in range(n):
    for j in range(n):
        surround = 0
        for dx, dy in zip(dxs, dys):
            if in_range(i+dx, j+dy, n) and matrix[i+dx][j+dy] == 1:
                surround += 1
        if surround >= 3:
            result += 1

print(result)