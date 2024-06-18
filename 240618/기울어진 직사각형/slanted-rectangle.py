n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 방향 정의: 오른쪽 아래, 오른쪽 위, 왼쪽 위, 왼쪽 아래
drs = [1, -1, -1, 1]
dcs = [1, 1, -1, -1]
max_total = 0

for r in range(n):
    for c in range(n):
        total = 0  # 시작 위치 값을 포함
        a = 0
        b = 0

        # 오른쪽 아래로 이동
        next_r = r
        next_c = c
        while in_range(next_r + drs[0], next_c + dcs[0]):
            next_r += drs[0]
            next_c += dcs[0]
            total += matrix[next_r][next_c]
            a += 1

        # 오른쪽 위로 이동
        while in_range(next_r + drs[1], next_c + dcs[1]):
            next_r += drs[1]
            next_c += dcs[1]
            total += matrix[next_r][next_c]
            b += 1

        # 왼쪽 위로 이동
        for _ in range(a):
            if in_range(next_r + drs[2], next_c + dcs[2]):
                next_r += drs[2]
                next_c += dcs[2]
                total += matrix[next_r][next_c]

        # 왼쪽 아래로 이동
        for _ in range(b):
            if in_range(next_r + drs[3], next_c + dcs[3]):
                next_r += drs[3]
                next_c += dcs[3]
                total += matrix[next_r][next_c]

            # 원래 위치로 돌아왔는지 확인
            if next_r == r and next_c == c and a >= 1 and b >= 1:
                max_total = max(total, max_total)

print(max_total)