n, k = map(int, input().split())

if k == 1:
    for i in range(1, n + 1):
        print((str(i)+' ') * n)
elif k == 2:
    for i in range(n):
        if i % 2 == 0:
            for j in range (1, n + 1):
                print(j, end=' ')
            print()
        else:
            for j in range (n, 0, -1):
                print(j, end=' ')
            print()
elif k == 3:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(j * i, end= ' ')
        print()