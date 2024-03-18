n = int(input())

def solve(n):
    if n == 0:
        return
    else:
        print("HelloWorld")
        solve(n - 1)

solve(n)