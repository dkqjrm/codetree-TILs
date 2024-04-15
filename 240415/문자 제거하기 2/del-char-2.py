a, n = input().split()
n = int(n)

for _ in range(n):
    idx = int(input())
    idx -= 1
    if idx < len(a):
        a = a[:idx] + a[idx + 1:]
        print(a)