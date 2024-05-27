# dp = [0] * 1005
# dp[0] = 0
# dp[1] = 0
# dp[2] = 1
# dp[3] = 1

# n = int(input())

# for i in range(4, n + 1):
#     dp[i] = dp[i-2] + dp[i-3]

# print(dp[n] % 10007)

n = int(input())
memo = [0] * 1005
memo[0] = 0
memo[1] = 0
memo[2] = 1
memo[3] = 1

def solve(n):
    if memo[n] != 0:
        return memo[n]
    
    memo[n] = memo[n-2] + memo[n-3]
    return memo[n]

print(solve(n))