OFFSET = 105
visited = [[0] * (OFFSET * 2) for _ in range(OFFSET * 2)]

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            visited[i][j] = 1
            # print(i, j)

result = 0
for i in visited:
    result += sum(i)
    
print(result)