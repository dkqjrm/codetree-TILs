n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [10005] * (m + 1)
dp[0] = 0

for num in array:
    for i in range(m, -1, -1):
        dp[i] = min(dp[i - num] + 1, dp[i])

# print(dp)

if dp[m] != 10005:
    print("Yes")
else:
    print("No")

# 5 10
# 5 7 10 12
# 5 7 9 10 11 12