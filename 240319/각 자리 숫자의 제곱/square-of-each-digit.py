n = int(input())

def solve(n):
    if n < 10:
        return n ** 2
    
    return solve(n // 10) + (n % 10) ** 2

print(solve(n))