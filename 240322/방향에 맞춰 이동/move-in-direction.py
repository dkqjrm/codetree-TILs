dx = {
    'N': 0,
    'E': 1,
    'W': -1,
    'S': 0}

dy = {
    'N': 1,
    'E': 0,
    'W': 0,
    'S': -1}

n = int(input())
x, y = 0, 0

for _ in range(n):
    direction, num = input().split()
    num = int(num)
    x += dx[direction] * num
    y += dy[direction] * num

print(x, y)