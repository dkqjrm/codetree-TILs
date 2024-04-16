n, m = map(int, input().split())

visited = [0] * (n + 1)
matrix = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

def dfs(vertex):
    visited[vertex] = 1
    for v in matrix[vertex]:
        if visited[v] == 0:
            visited[v] = 1

dfs(1)
print(sum(visited) - 1)