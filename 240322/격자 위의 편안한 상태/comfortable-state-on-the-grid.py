n, m = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n+1)]

def in_range(r, c, n):
    return 1 <= r and r <= n and 1 <= c and c <= n
drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]


for _ in range(m):
    r, c = map(int, input().split())
    matrix[r][c] = 1
    count = 0
    for dr, dc in zip(drs, dcs):
        move_r = r + dr
        move_c = c + dc    
        if in_range(move_r, move_c, n) and matrix[move_r][move_c] == 1:
            count += 1
    
    if count == 3:
        print(1)
    else:
        print(0)