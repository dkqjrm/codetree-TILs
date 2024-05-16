m = int(input())
n = int(input())

dp = [0] * (m + 1)
dp[0] = 1

coins = [list(map(int, input().split())) for _ in range(n)]

for p, k in coins: # 동전 순서대로
    for current_money in range(m, -1, -1):
        for count in range(1, k + 1):
            if current_money + p * count <= m:
                # dp[current_money + p * count] += dp[current_money]
                dp[current_money + p * count] = (dp[current_money + p * count] + dp[current_money]) % 1,000,000,007

            else:
                break

print(dp[m])