n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (m + 1)
dp[0] = 0
# dp[i] 무게 i일 때 얻을 수 있는 최대의 가치

for w, v in array:
    for i in range(m, -1, -1):
        if i - w >= 0 and dp[i - w] != -1:
            dp[i] = max(dp[i - w] + v, dp[i])

num = max(dp[:m])
if num != -1:
    print(num)
else:
    print(0)