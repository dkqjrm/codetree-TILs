n = int(input())

dr = [0,1,0,-1]
dc = [-1,0,1,0]

matrix = [[0] * n for _ in range(n)]

def in_range(r, c, n):
    return 0 <= r and r < n and 0 <= c and c < n

r, c = n-1, n-1
idx = n*n
direction = 0
matrix[r][c] = idx

while idx != 1:
    move_r = r + dr[direction]
    move_c = c + dc[direction]

    if in_range(move_r, move_c, n) and matrix[move_r][move_c] == 0:
        r = move_r
        c = move_c
        idx -= 1
        matrix[r][c] = idx
    else:
        direction = (direction + 1) % 4

for row in matrix:
    print(*row)