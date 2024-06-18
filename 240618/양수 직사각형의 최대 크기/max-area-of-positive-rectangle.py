n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 겹치는지 확인
def check_duplicate(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return True
    return False

max_size = -1
# 첫번째 사각형의 좌상단 좌표를 잡고, 우하단 좌표를 잡는다.
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                total = 0
                flag = True
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        if array[i][j] < 0:
                            flag = False
                            break
                size = ((x2 - x1) + 1) * ((y2 - y1) + 1)
                if flag is True and size >= max_size:        
                    max_size = size

print(max_size)
# 두번째 사각형의 좌상단 좌표를 잡고 우하단 좌표를 잡는다.

# 둘이 비교 겹치는지 확인, 안겹치면 최대합 갱신.