n, m = map(int, input().split())
array = list(map(int, input().split()))

# dp[i] 는 i를 만들기 위해 사용되는 최소 순열의 길이
# 근데 사실 순서가 뭐가 중요한지 모르겠네,, 그냥 구하면 될듯.. 5 2 4 1이나 1 2 4 5 나 어차피 중복 수가 없으니까.

dp = [10005] * (m + 1)
dp[0] = 0

# for i in range(m):
#     for num in array:
#         if i + num <= m:
#             dp[i + num] = min(dp[i + num], dp[i] + 1) # 이렇게 하면 중복이 반영된다.

for num in array:
    for i in range(m, -1, -1):
        dp[i] = min(dp[i - num] + 1, dp[i])

if dp[m] != 10005:
    print(dp[m])
else:
    print(-1)