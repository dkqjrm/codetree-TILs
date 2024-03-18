n = int(input())

def solve(n):
    if n == 0:
        return
    else:
        print(n, end=' ')
        solve(n - 1)
        print(n, end=' ')

solve(n)