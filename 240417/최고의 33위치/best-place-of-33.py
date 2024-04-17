n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < 3 and 0 <= y < 3

drs = [-1, 1, 0, 0, -1, -1, 1, 1]
dcs = [0, 0, -1, 1, -1, 1, -1, 1]

max_total = 0

for i in range(n):
    for j in range(n):
        total = matrix[i][j]
        for dr, dc in zip(drs, dcs):
            nr = i + dr
            nc = j + dc
            if in_range(nr, nc):
                total += matrix[nr][nc]
        # print(total)
        max_total = max(total, max_total)
    
print(max_total)