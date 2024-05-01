# 트로미노
# n * m 크기의 이차원 영역의 각 위치에 자연수가 하나씩 적혀있습니다.
# 이때 2가지 종류의 블럭 중 "한 개"를 블럭의 격자를 벗어나지 않도록 적당히 올려놓아 블럭이 놓인 칸 앞에 적힌 숫자의 합이 최대가 될 떄의 결과를 출력
# 단,  주어진 블럭은 자유롭게 회전하거나 뒤집을 수 있습니다.

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

dr = [
    [1, 0],
    [1, 0],
    [-1, 0],
    [-1, 0],
    [0, 1],
    [0, 1],
    [0, -1],
    [0, -1],
    [1, 1],
    [-1, -1],
    [0, 0],
    [0, 0]
]

dc = [
    [0, 1],
    [0, -1],
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [1, 0],
    [-1, 0],
    [0, 0],
    [0, 0],
    [1, 1],
    [-1, -1]
]

def checking(r, c):
    return 0 <= r < n and 0 <= c < m

max_total = -1

for r in range(n):
    for c in range(m):
        for tmp in zip(dr, dc):
            total = matrix[r][c]
            nr = r
            nc = c
            for t_r, t_c in tmp:
                nr += t_r
                nc += t_c
                if checking(nr, nc):
                    total += matrix[nr][nc]
            max_total = max(total, max_total)

print(max_total)