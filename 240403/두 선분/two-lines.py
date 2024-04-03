x1, x2, x3, x4 = map(int, input().split())

def solve(x1, x2, x3, x4):
    visited = [0] * 101
    for i in range(x1, x2 + 1):
        visited[i] = 1
    for j in range(x3, x4 + 1):
        if visited[i] == 1:
            return "intersecting"
    
    return "nonintersecting"

print(solve(x1, x2, x3, x4))