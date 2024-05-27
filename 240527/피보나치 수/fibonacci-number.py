n = int(input())

# dp = [0] * 50

# dp[0] = 0
# dp[1] = 1

# for i in range(2, n + 1):
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[n])

def solve(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return solve(n-1) + solve(n-2)

print(solve(n))