OFFSET = 205
visited = [[0] * (OFFSET * 2) for _ in range(OFFSET * 2)]

n = int(input())
dx, dy = 8, 8

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            visited[i][j] = 1

result = 0
for i in visited:
    result += sum(i)

print(result)