n = int(input())
array = list(map(int, input().split()))
# 한 번에 정확히 1계단 혹은 2계단 단위로 올라갈 수 있음.
# 그런데 계단을 1개씩 올라가는건 최대 3번만 하고 싶음.

dp = [[-10000000] * 3 for _ in range(n)]

# dp[i] = max(dp[i - 1], dp[i - 2]) + array[i]
# 인데, 여기에 j를 추가해서 1번씩 몇번이나 뛰었는지 확인을 해야 할 것 같음.
# dp[i][j] = max(dp[i - 1][j - 1], dp[i - 2][j])


dp[0][1] = array[0]
dp[1][0] = array[1]

for i in range(2, n):
    for j in range(3):
        if j != 0:
            dp[i][j] = dp[i - 1][j - 1]
        dp[i][j] = max(dp[i][j],  dp[i - 2][j]) + array[i]


# for i in dp:
#     print(*i)
print(max(dp[-1]))