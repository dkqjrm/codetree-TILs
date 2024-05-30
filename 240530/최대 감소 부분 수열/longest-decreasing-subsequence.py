n = int(input())
array = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))