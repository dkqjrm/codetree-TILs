n = int(input())
A = list(map(int, input().split()))

A.sort()
print(*A)
print(*A[::-1])