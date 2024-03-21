OFFSET = 200

n = int(input())
visited = [0] * 410

def move(location, x, arrow):
    if arrow == 'L':
        after_location = location - int(x)
        for i in range(location - 1, after_location - 1, -1): # 6L 이면 201 201 200 109 108 107을 체크함.
            visited[i] += 1

    else:
        after_location = location + int(x)
        for i in range(location, after_location): # 2R 이면 200, 201을 체크함
            visited[i] += 1

    return after_location
            
location = OFFSET
for _ in range(n):
    x, arrow = input().split()
    location = move(location, x, arrow)

result = 0
for i in visited:
    if i >= 2:
        result += 1

print(result)