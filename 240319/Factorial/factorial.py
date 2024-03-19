n = int(input())

def solve(n):
    if n in [0, 1]:
        return 1
    
    return solve(n-1) * n

print(solve(n))