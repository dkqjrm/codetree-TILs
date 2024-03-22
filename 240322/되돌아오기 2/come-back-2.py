instruction = input()

x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 처음엔 북쪽
direction = 0
time = 0
result_time = -1

for cha in instruction:
    if cha == 'F':
        x += dx[direction]
        y += dy[direction]
    elif cha == 'R':
        direction = (direction + 1) % 4
    elif cha == 'L':
        direciton = (direction + 3) % 4
    time += 1
    if x == 0 and y == 0 and result_time == -1:
        result_time = time        

print(result_time)