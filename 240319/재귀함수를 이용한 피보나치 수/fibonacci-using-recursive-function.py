n = int(input())

def solve(n):
    if n in [1, 2]:
        return 1
    
    return solve(n - 2) + solve(n - 1)

print(solve(n))