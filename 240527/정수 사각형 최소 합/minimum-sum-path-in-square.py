n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][n-1] = array[0][n-1]

for i in range(1, n):
    dp[0][n-i-1] = dp[0][n-i-1+1] + array[0][n-1-i]
    dp[i][n-1] = dp[i-1][n-1] + array[i][n-1]

for c in range(n-2, -1, -1):
    for r in range(1, n):
        dp[r][c] = min(dp[r-1][c], dp[r][c+1]) + array[r][c]

print(min(dp[-1][0]))