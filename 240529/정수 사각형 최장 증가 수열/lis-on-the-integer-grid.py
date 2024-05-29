n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]

    max_move = 1
    for dr, dc in zip(drs, dcs):
        next_r = r + dr
        next_c = c + dc
        if in_range(next_r, next_c) and matrix[next_r][next_c] > matrix[r][c]:
            max_move = max(max_move, 1 + dfs(next_r, next_c))

    dp[r][c] = max_move
    return dp[r][c]

max_result = 0
for r in range(n):
    for c in range(n):
        max_result = max(max_result, dfs(r, c))  # 모든 셀에 대해 최대 이동 거리 계산

print(max_result)