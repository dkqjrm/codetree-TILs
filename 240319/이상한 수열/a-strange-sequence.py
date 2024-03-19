n = int(input())

def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return solve(n // 3) + solve(n-1)


print(solve(n))