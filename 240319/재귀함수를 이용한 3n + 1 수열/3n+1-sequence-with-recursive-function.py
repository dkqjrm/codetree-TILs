n = int(input())

def solve(n, cnt):
    if n == 1:
        return cnt
    else:
        if n % 2 == 0:
            return solve(n // 2, cnt + 1)

        else:
            return solve(n * 3 + 1, cnt + 1)


print(solve(n, 0))