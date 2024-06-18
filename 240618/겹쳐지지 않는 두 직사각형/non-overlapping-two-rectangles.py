n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 겹치는지 확인
def check_duplicate(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return True
    return False

max_total = -1e12
# 첫번째 사각형의 좌상단 좌표를 잡고, 우하단 좌표를 잡는다.
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                for x3 in range(n):
                    for y3 in range(m):
                        for x4 in range(x3, n):
                            for y4 in range(y3, m):
                                if check_duplicate(x1, y1, x2, y2, x3, y3, x4, y4):
                                    total = 0
                                    for i in range(x1, x2 + 1):
                                        for j in range(y1, y2 + 1):
                                            total += array[i][j]
                                    for i in range(x3, x4 + 1):
                                        for j in range(y3, y4 + 1):
                                            total += array[i][j]
                                    max_total = max(total, max_total)

print(max_total)
# 두번째 사각형의 좌상단 좌표를 잡고 우하단 좌표를 잡는다.

# 둘이 비교 겹치는지 확인, 안겹치면 최대합 갱신.