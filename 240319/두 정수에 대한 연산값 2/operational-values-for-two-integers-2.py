a, b = map(int, input().split())

def solve(a, b):
    if a < b:
        return a + 10, b * 2
    else:
        return a * 2, b + 10

print(*solve(a, b))