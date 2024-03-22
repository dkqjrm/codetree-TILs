x, y = 0, 0

instruction = input()
dx = [0, 1, 0, -1] # 북 동 남 서
dy = [1, 0 ,-1, 0] # 북 동 남 서
direction = 0
for cha in instruction:

    if cha == 'R':
        direction += 1
    elif cha == 'L':
        direction -= 1
    else:
        x += dx[(0 + direction + 800000) % 4]
        y += dy[(0 + direction + 800000) % 4]

print(x, y)