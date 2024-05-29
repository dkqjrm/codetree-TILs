n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = matrix[0][0]

drs = [-1, 0] # 상, 좌
dcs = [0, -1] # 상, 좌

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

for r in range(n):
    for c in range(n):
        for dr, dc in zip(drs, dcs):
            if in_range(r + dr, c + dc):
                dp[r][c] = max(dp[r][c], dp[r + dr][c + dc])
        dp[r][c] = min(matrix[r][c], dp[r][c])

print(dp[n-1][n-1])