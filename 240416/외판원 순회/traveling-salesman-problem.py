# 2, 3, 4
# 3, 4
# 4
# 1 이런식으로 가야하네
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * (n + 1)

results = []
result = []

def check(num):
    if num == n + 1:
        # print(*result)
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
min_total = 1e12

for result in results:
    if result[-1] == 0:
        total = 0
        now = 0
        for i in result:
            total += matrix[now][i]
            now = i
        min_total = min(total, min_total)



print(min_total)