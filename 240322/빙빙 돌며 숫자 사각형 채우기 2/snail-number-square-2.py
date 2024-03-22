row, column = map(int, input().split())

matrix = [[0] * column for _ in range(row)]

def in_range(r, c, row, column):
    return 0 <= r and r < row and 0 <= c and c < column

dr = [1, 0, -1, 0] # 남 동 북 서
dc = [0, 1, 0, -1] # 남 동 북 서

direction = 0

r, c = 0, 0
idx = 1
matrix[r][c] = idx
while idx != (row * column):
    move_r = r + dr[direction]
    move_c = c + dc[direction]
    if in_range(move_r, move_c, row, column) and matrix[move_r][move_c] == 0:
        r = move_r
        c = move_c
        idx += 1
        matrix[r][c] = idx
    else:
        direction = (direction + 1) % 4


for rows in matrix:
    print(*rows)