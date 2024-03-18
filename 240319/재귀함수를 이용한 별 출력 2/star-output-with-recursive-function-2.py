n = int(input())

def solve(n):
    if n == 0:
        return
    else:
        print('* ' * n)
        solve(n-1)
        print('* ' * n)

solve(n)