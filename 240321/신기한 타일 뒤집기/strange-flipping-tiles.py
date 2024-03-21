OFFSET = (1000 * 100 + 1)

visited = [0] * (OFFSET * 2)
n = int(input())

def move(location, x, direction):
    x = int(x)

    if direction == 'L':
        visited[location] = 1
        for _ in range(1, x):
            location -= 1
            visited[location] = 1

    else:
        visited[location] = 2
        for _ in range(1, x):
            location += 1
            visited[location] = 2

    return location

location = OFFSET

for _ in range(n):
    x, direction = input().split()
    location = move(location, x, direction)

print(f'{visited.count(1)} {visited.count(2)}')