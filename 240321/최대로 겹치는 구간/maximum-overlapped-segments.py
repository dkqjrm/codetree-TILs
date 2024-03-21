OFFSET = 200

n = int(input())
visited = [0] * (300 + OFFSET)


for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1 + OFFSET, x2 + OFFSET):
        visited[i + OFFSET] += 1

print(max(visited))