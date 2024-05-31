# 지금까지 선택한 동전의 합이 같다면, 지금까지 사용한 동전의 개수가 많을수록 더 좋다.

n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [1e12] * (m + 1)
dp[0] = 1
for coin in coins:
    if coin < m:
        dp[coin] = 1

for i in range(max(coins), m + 1):
    for coin in coins:
        dp[i] = min(dp[i], dp[i-coin] + 1)

coin = dp[m]

if coin == 1e12:
    print(-1)
else:
    print(coin)