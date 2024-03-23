n, t = map(int, input().split())

instruction = input()

matrix = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r, c = n // 2, n // 2
direction = 0
result = matrix[r][c]

def in_range(r, c, n):
    return 0 <= r and r < n and 0 <= c and c < n

for cha in instruction:
    if cha == 'F':
        move_r = r + dr[direction]
        move_c = c + dc[direction]

        if in_range(move_r, move_c, n):
            r = move_r
            c = move_c
            result += matrix[r][c]

    elif cha == 'L':
        direction = (direction + 3) % 4

    elif cha == 'R':
        direction = (direction + 1) % 4

print(result)