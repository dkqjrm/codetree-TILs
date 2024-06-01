n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [-1] * (m + 1)
dp[0] = 0

for coin in coins:
    for i in range(m):
        if dp[i] != -1 and i + coin <= m:
            dp[i + coin] = max(dp[i + coin], dp[i] + 1)

# print(dp)
print(dp[m])