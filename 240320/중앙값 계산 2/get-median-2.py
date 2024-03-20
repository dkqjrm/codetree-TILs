n = int(input())

A_list = list(map(int, input().split()))
for idx in range(n):
    if (idx + 1) % 2 == 1:
        print(sorted(A_list[:idx + 1])[((idx)//2)], end=' ')