n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

dp[0][0] = array[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + array[i][0]
    dp[0][i] = dp[0][i-1] + array[0][i]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + array[i][j]


print(max(dp[-1]))