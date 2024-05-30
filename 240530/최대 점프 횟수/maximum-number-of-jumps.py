n = int(input())
array = list(map(int, input().split()))
dp = [-1] * n
dp[0] = 0

def in_range(idx):
    return 0 < idx < n

for i in range(1, n):
    for j in range(i):
        if dp[j] != -1 and j + array[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)
        

print(max(dp))
# print(dp)