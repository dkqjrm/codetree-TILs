n = int(input())

# dp = [0] * 50

# dp[0] = 0
# dp[1] = 1

# for i in range(2, n + 1):
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[n])

memo = [-1 for _ in range(n+1)]

def solve(n):
    if memo[n] != -1:
        return memo[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    memo[n] = solve(n-1) + solve(n-2)
    
    return memo[n]

print(solve(n))