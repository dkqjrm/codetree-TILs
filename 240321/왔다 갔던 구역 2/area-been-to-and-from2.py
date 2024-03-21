OFFSET = 200

n = int(input())
visited = [0] * 410

def move(location, x, arrow):
    if arrow == 'L':
        after_location = location - int(x)
        for i in range(location, after_location, -1):
            visited[i] += 1

    else:
        after_location = location + int(x)
        for i in range(location, after_location):
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