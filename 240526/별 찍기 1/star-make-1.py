a, b = map(int, input().split())

if b == 1:
    for i in range(1, a + 1):
        print('*' * i)
if b == 2:
    for i in range(a, 0, -1):
        print('*' * i)
if b == 3:
    for i in range(a - 1, -1, -1): # 4 3 2 1 0
        print(' '*i, end='')

        print('*'*(2*(5-i)-1))