OFFSET = 2000
visited = [[0] * (OFFSET * 2) for _ in range(OFFSET * 2)]

a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
a_x1, a_y1, a_x2, a_y2 = a_x1 + OFFSET, a_y1 + OFFSET, a_x2 + OFFSET, a_y2 + OFFSET
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = b_x1 + OFFSET, b_y1 + OFFSET, b_x2 + OFFSET, b_y2 + OFFSET

for i in range(a_x1, a_x2):
    for j in range(a_y1, a_y2):
        visited[i][j] = 1


for i in range(b_x1, b_x2):
    for j in range(b_y1, b_y2):
        visited[i][j] = 0

min_x = 1e9
max_x = 0
min_y = 1e9
max_y = 0

for i in range(a_x1, a_x2):
    for j in range(a_y1, a_y2):
        if visited[i][j] == 1:
            if i < min_x:
                min_x = i
            if j < min_y:
                min_y = j
            if i > max_x:
                max_x = i
            if j > max_y:
                max_y = j
if min_x == 1e9:
    min_x = 0
if min_y == 1e9:
    min_y = 0

print((max_x + 1 - min_x) * (max_y + 1 - min_y))