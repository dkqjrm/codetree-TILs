n, m = map(int, input().split())

matrix = [list(map(int,input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

drs = [0, 1] # 우 상
dcs = [1, 0] # 우 상

def in_range(r, c):
    if 0 <= r < m and 0 <= c < n:
        return True
    else:
        return False

def dfs(r, c):
    for dr, dc in zip(drs, dcs):
        if in_range(r + dr, c + dc) and matrix[r + dr][c + dc] == 1 and visited[r + dr][c + dc] == 0:
            visited[r + dr][c + dc] = 1
            # print(r + dr, c + dc)
            dfs(r + dr, c + dc)

dfs(0, 0)

if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)