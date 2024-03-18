n, m = map(int, input().split())
A = list(map(int, input().split()))
def solve(a1, a2):
    result = 0
    for i in range(a1-1, a2):
        result += A[i]

    return result

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(solve(a1, a2))