n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n - 1):
    for j in range(n - 1):
        num = array[i][j]
        cnt = dp[i][j]
        for k in range(i + 1, n):
            for l in range(j + 1, n):
                if array[k][l] > num:
                    dp[k][l] = max(dp[k][l], cnt + 1)

print(max([max(i) for i in dp]))