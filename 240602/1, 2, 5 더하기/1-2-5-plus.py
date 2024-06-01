n = int(input())
array = [1, 2, 5]
dp = [0] * (n + 1)
dp[0] = 1
# dp[sum]은 sum을 나타낼 수 있는 모든 방법

for i in range(n + 1):
    for num in array:
        dp[i] += dp[i - num] % 10007

print(dp[-1])