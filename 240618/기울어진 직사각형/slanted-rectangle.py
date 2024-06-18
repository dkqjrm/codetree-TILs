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
        for a in range(1, n):
            for b in range(1, n):
                total = matrix[r][c]  # 시작 위치 값을 포함
                valid = True
                
                next_r, next_c = r, c

                # 오른쪽 아래로 이동
                for _ in range(a):
                    next_r += drs[0]
                    next_c += dcs[0]
                    if not in_range(next_r, next_c):
                        valid = False
                        break
                    total += matrix[next_r][next_c]
                if not valid:
                    continue

                # 오른쪽 위로 이동
                for _ in range(b):
                    next_r += drs[1]
                    next_c += dcs[1]
                    if not in_range(next_r, next_c):
                        valid = False
                        break
                    total += matrix[next_r][next_c]
                if not valid:
                    continue

                # 왼쪽 위로 이동
                for _ in range(a):
                    next_r += drs[2]
                    next_c += dcs[2]
                    if not in_range(next_r, next_c):
                        valid = False
                        break
                    total += matrix[next_r][next_c]
                if not valid:
                    continue

                # 왼쪽 아래로 이동
                for _ in range(b):
                    next_r += drs[3]
                    next_c += dcs[3]
                    if not in_range(next_r, next_c):
                        valid = False
                        break
                    if next_r == r and next_c == c:
                        break  # 다시 시작점으로 돌아왔을 때 더하지 않도록 중단
                    total += matrix[next_r][next_c]
                if not valid:
                    continue

                # 원래 위치로 돌아왔는지 확인
                if next_r == r and next_c == c:
                    max_total = max(max_total, total)

print(max_total)