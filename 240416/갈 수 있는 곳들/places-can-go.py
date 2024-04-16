from collections import deque

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
starting_points = [list(map(int, input().split())) for _ in range(k)]

drs = [1, -1, 0, 0]
dcs = [0, 0, -1, 1]

q = deque()

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

cnt = 0

for starting_point in starting_points:
    starting_point[0] -= 1
    starting_point[1] -= 1
    if visited[starting_point[0]][starting_point[1]] == 0 and matrix[starting_point[0]][starting_point[1]] == 0:
        q.append([starting_point[0], starting_point[1]])
        visited[starting_point[0]][starting_point[1]] = 1
        cnt += 1

        while q:
            r, c = q.popleft()
            for dr, dc in zip(drs, dcs):
                next_r = r + dr
                next_c = c + dc
                if in_range(next_r, next_c) and matrix[next_r][next_c] == 0 and visited[next_r][next_c] == 0:
                    q.append([next_r, next_c])
                    visited[next_r][next_c] = 1
                    cnt += 1

print(cnt)