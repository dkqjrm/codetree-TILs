n = int(input())

def solve(n):
    if n in [1, 2]:
        return n

    return solve(n - 2) + n

print(solve(n))