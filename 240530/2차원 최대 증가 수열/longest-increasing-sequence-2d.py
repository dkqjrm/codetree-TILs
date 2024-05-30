n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dp[0][0] = 1

for i in range(n - 1):
    for j in range(m - 1):
        num = array[i][j]
        cnt = dp[i][j]
        if dp[i][j] == -1:
            continue

        for k in range(i + 1, n):
            for l in range(j + 1, m):
                if array[k][l] > num:
                    dp[k][l] = max(dp[k][l], cnt + 1)

# for i in dp:
#     print(*i)
print(max([max(i) for i in dp]))