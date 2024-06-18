n, m, q = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
winds = [list(map(int, input().split())) for _ in range(q)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def mean_value(r, c, prev_array):
    many = 1
    total = prev_array[r][c]
    drs = [-1, 0, 1, 0] # 상 우 하 좌
    dcs = [0, 1, 0, -1]

    for dr, dc in zip(drs, dcs):
        if in_range(r + dr, c + dc):
            many += 1
            total += prev_array[r + dr][c + dc]
    
    return total // many


# 바람이 불 때 array를 시계방향으로 움직이는 함수
def move_array(r1, c1, r2, c2):
    now_value = array[r1][c1]
    # 위측
    for c in range(c1 + 1, c2 + 1):
        next_value = array[r1][c]
        array[r1][c] = now_value
        now_value = next_value
    # 우측
    for r in range(r1 + 1, r2 + 1):
        next_value = array[r][c2]
        array[r][c2] = now_value
        now_value = next_value
    # 아래측
    for c in range(c2 - 1, c1 - 1, - 1):
        next_value = array[r2][c]
        array[r2][c] = now_value
        now_value = next_value
    # 좌측
    for r in range(r2 - 1, r1 - 1, -1):
        next_value = array[r][c1]
        array[r][c1] = now_value
        now_value = next_value
    prev_array = []
    for i in array:
        prev_array.append(i[:])

    # 위측
    for c in range(c1, c2 + 1):
        for r in range(r1, r2 + 1):
            array[r][c] = mean_value(r, c, prev_array)

    # print(prev_array)


for wind in winds:
    r1, c1, r2, c2 = wind
    move_array(r1 - 1, c1 - 1, r2 - 1, c2 - 1)

for i in array:
    print(*i)