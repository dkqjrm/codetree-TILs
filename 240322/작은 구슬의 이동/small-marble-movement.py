n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c) # 0 1

matrix = [[0] * n for _ in range(n + 1)]

dc = {
    'U': 0,
    'D': 0,
    'R': 1,
    'L': -1
}

dr = {
    'U': -1,
    'D': 1,
    'R': 0,
    'L': 0,
}

def in_range(r, c, n):
    return 1 <= r and r <= n and 1 <= c and c <= n

for _ in range(t):
    move_r = r + dr[d]
    move_c = c + dc[d] 
    # 만약 이동하려는 곳이 range 안이라면 앞으로 이동
    if in_range(move_r, move_c, n):
        r = move_r
        c = move_c
    # 밖이라면 방향 전환
    else:
        if d == 'U':
            d = 'D'
        elif d == 'R':
            d = 'L'
        elif d == 'D':
            d = 'U'
        elif d == 'L':
            d = 'R'

print(r, c) # 0 2