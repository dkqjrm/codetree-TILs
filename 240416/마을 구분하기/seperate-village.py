n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

drs = [1, -1, 0, 0] # 상 하 좌 우
dcs = [0, 0, -1, 1] # 상 하 좌 우

def in_range(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

total_num = []

def dfs(r, c):
    for dr, dc in zip(drs, dcs):
        if in_range(r + dr, c + dc) and matrix[r + dr][c + dc] == 1 and visited[r + dr][c + dc] == 0:
            visited[r + dr][c + dc] = 1
            dfs(r + dr, c + dc)


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and matrix[i][j] == 1:
            tmp_num = sum(sum(visited,[]))
            dfs(i, j)
            tmp_num = abs(tmp_num - sum(sum(visited,[])))
            total_num.append(tmp_num)

print(len(total_num))
for i in sorted(total_num):
    print(i)