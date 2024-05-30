n = int(input())
array = list(map(int, input().split()))
dp = [0] * n

def in_range(idx):
    return 0 < idx < n

for i in range(n):
    for j in range(1, array[i] + 1):
        idx = i + j
        if in_range(idx):
            dp[idx] = max(dp[i] + 1, dp[idx])

# print(dp)
num = 0
for i in range(1, n):
    if dp[i] != 0:
        num = max(num, dp[i])
    else:
        break

print(num)