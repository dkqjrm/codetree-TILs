from collections import deque

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
q = deque()

r, c = map(int, input().split())
r -= 1
c -= 1

q.append([r, c])
# r, c에서 시작해서 bfs를 할 때 지금 가고 있는 곳보다 작은 곳으로 이동해야함.
# 그러면서, row 값이 적은 곳 -> column 값이 적은 곳

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

drs = [1, -1, 0, 0]
dcs = [0, 0, -1, 1]

tmp_array = []

cnt = 0
while cnt != k:
    value = matrix[r][c]
    visited = [
        [[0,-1,-1,-1] for _ in range(n)]
        for _ in range(n)]

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr = r + dr
            nc = c + dc
            if in_range(nr, nc) and matrix[nr][nc] < value and visited[nr][nc] == [0, -1, -1, -1]:
                visited[nr][nc] = [1, nr, nc, matrix[nr][nc]]
                q.append([nr, nc])


    # visited.sort(key = lambda x : (-x[0][3], x[0][1], x[0][2]))
    tmp = sorted(sum(visited, []), key = lambda x : (-x[3], x[1], x[2]))[0]
    # print(tmp)
    r = tmp[1]
    c = tmp[2]
    cnt += 1
    q.append([r, c])
print(r + 1, c + 1)