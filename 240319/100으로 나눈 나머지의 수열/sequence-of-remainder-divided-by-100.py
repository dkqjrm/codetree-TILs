n = int(input())

def solve(i):
    if i == 1:
        return 2
    elif i == 2:
        return 4
    
    return (solve(i-2) * solve(i-1)) % 100

print(solve(n))