n, m = map(int, input().split())

A = [0]
B = [0]

for _ in range(n):
    d, t = input().split()
    t = int(t)
    if d == 'L':
        for i in range(t):
            A.append(A[-1] - 1)

    else:
        for i in range(t):
            A.append(A[-1] + 1)

for _ in range(m):
    d, t = input().split()
    t = int(t)
    if d == 'L':
        for i in range(t):
            B.append(B[-1] - 1)

    else:
        for i in range(t):
            B.append(B[-1] + 1)

check = -1
for idx in range(1, len(A)):
    if A[idx] == B[idx]:
        check = idx
        break

print(check)