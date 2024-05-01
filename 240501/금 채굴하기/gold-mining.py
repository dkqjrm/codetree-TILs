# n x n크기의 이차원 영역에 파묻힌 금을 손해를 보지 않는 선에서 최대한 많이 채굴.
# 채굴은 마름모 모양으로 한번만 가능함.
# 마름모 모양이란 특정 중심점을 기준으로 K번 이내로 상하좌우의 인접한 곳으로 이동하는 것을 반복했을 떄 갈 수 있는 모든 영역
# 채굴에 드는 비용은 마름모 안의 격자 갯수만큼 들어가며 K * K + (K + 1)*(K + 1)로 계산 가능 함.
# 손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def check(r, c):
    return 0 <= r < n and 0 <= c < n

drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

def solve(r, c, k):
    global total
    if k == 0:
        visited[r][c] = 1
        return

    for dr, dc in zip(drs, dcs):
        nr = r + dr
        nc = c + dc
        if check(nr, nc) and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            if matrix[nr][nc] == 1:
                total += 1
            solve(nr, nc, k- 1)

    

max_total = 0

for r in range(n):
    for c in range(n):
        for k in range(20):
            visited = [[0] * n for _ in range(n)]
            total = 0
            cost = k ** 2 + (k + 1) ** 2
            solve(r, c, k)
            # print(total)
            if cost - total * m >= 0:
                max_total = max(total, max_total)
            # print(*visited)

print(max_total)