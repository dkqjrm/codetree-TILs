num, shape = map(int, input().split())

def solve(num, shape):
    if shape == 1:
        for i in range(1, num // 2 + 1):
            print('*' * i)
        print('*' * (num // 2 + 1))
        for i in range(num // 2, 0, -1):
            print('*' * i)
    elif shape == 2:
        for i in range(num // 2, 0, -1):
            print(' ' * i, end='')
            print('*' * (num // 2 - i + 1))
        print('*' * (num // 2 + 1))
        for i in range(1, num // 2 + 1):
            print(' ' * i, end='')
            print('*' * (num // 2 - i + 1))
    elif shape == 3: 
        for i in range(num, -1, -2):
            print(' ' * ((num - i) // 2), end='')
            print('*' * i)
        for i in range(3, num + 1, 2):
            print(' ' * ((num - i) // 2), end='')
            print('*' * i)
    elif shape == 4:
        for i in range(num // 2, -1, -1):
            print(' ' * ((num // 2) - i), end='')
            print("*" * (i + 1))
        for i in range(1, (num // 2) + 1):
            print(' ' * (num // 2), end='')
            print('*' * (i + 1))

solve(num, shape)