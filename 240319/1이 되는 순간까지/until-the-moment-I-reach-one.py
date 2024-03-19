n = int(input())

def solve(n):
    if n == 1:
        return 0
    
    else:
        if n % 2 == 0:
            return solve(n // 2) + 1
        else:
            return solve(n // 3) + 1

print(solve(n))