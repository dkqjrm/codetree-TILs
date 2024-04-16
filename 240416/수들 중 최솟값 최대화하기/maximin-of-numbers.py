n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * (n + 1)

results = []
result = []

def check(num):
    if num == n + 1:
        results.append(result[:])
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            result.append(i)

            check(num + 1)

            result.pop()
            visited[i] = 0

check(1)

max_result = -1e12

for result in results:
    total = []
    for x, y in enumerate(result):
        total.append(matrix[x][y])
    max_result = max(max_result, min(total))

print(max_result)