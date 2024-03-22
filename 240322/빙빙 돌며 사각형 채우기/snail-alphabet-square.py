row, column = map(int, input().split())

matrix = [[0] * column for _ in range(row)]

def in_range(r, c, row, column):
    return 0 <= r and r < row and 0 <= c and c < column

dr = [0, 1, 0, -1] # 동 남 서 북
dc = [1, 0, -1, 0] # 동 남 서 북

direction = 0

r, c = 0, 0

idx = 0
char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*1000
matrix[r][c] = char_list[idx]
while idx != (row * column)-1:
    move_r = r + dr[direction]
    move_c = c + dc[direction]
    if in_range(move_r, move_c, row, column) and matrix[move_r][move_c] == 0:
        r = move_r
        c = move_c
        idx += 1
        matrix[r][c] = char_list[idx]
    else:
        direction = (direction + 1) % 4


for rows in matrix:
    print(*rows)