n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

drs = [1, -1, 0, 0]
dcs = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def dfs(r, c, num):
    visited[r][c] = 1

    for dr, dc in zip(drs, dcs):
        if in_range(r + dr, c + dc) and matrix[r + dr][c + dc] > num and visited[r + dr][c + dc] == 0:
            visited[r + dr][c + dc] = 1
            dfs(r + dr, c+ dc, num)

total_num = []

for num in range(1, max(sum(matrix, [])) + 1):
    visited = [[0] * m for _ in range(n)]
    tmp_num = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > num and visited[i][j] == 0:
                dfs(i, j, num)
                tmp_num += 1
    total_num.append(tmp_num)

# print(total_num)
for idx, i in enumerate(total_num, start = 1):
    if i == max(total_num):
        print(idx, i)