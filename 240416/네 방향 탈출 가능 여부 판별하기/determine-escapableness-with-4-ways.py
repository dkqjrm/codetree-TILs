from collections import deque


q = deque()
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q.append([0, 0])
visited[0][0] = 1

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

drs = [1, -1, 0, 0]
dcs = [0, 0, -1, 1]

while q:
    curr_v = q.popleft()
    for dr, dc in zip(drs, dcs):
        next_r = curr_v[0] + dr
        next_c = curr_v[1] + dc
        if in_range(next_r, next_c) and matrix[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
            q.append([next_r, next_c])
            visited[next_r][next_c] = 1


print(int(visited[n-1][m-1] == 1))