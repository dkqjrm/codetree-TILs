n = int(input())
x, y = 0, 0

dx = {
    'N': 0,
    'E': 1,
    'S': 0,
    'W': -1
}

dy = {
    'N': 1,
    'E': 0,
    'S': -1,
    'W': 0
}

def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

check = False
result_time = -1
time = 0
for _ in range(n):
    direciton, num = input().split()
    num = int(num)

    for __ in range(num):
        time += 1
        move_x = x + (dx[direciton])
        move_y = y + (dy[direciton])

        if in_range(move_x, move_y, n):
            x = move_x
            y = move_y
        if check is False and x == 0 and y == 0:
            check = True
            result_time = time
        

print(result_time)