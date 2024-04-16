n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

drs = [1, -1, 0, 0]
dcs = [0, 0, -1, 1]

max_cnt = 0
cnt = 1

def dfs(r, c, num):
    global cnt
    visited[r][c] = 1
    
    for dr, dc in zip(drs, dcs):
        new_r = r + dr
        new_c = c + dc
    
        if in_range(new_r, new_c) and matrix[new_r][new_c] == num and visited[new_r][new_c] == 0:
            visited[new_r][new_c] = 1
            dfs(new_r, new_c, num)
            cnt += 1

total = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 1
            dfs(i, j, matrix[i][j])
            if cnt >= 4:
                total += 1
            max_cnt = max(cnt, max_cnt)
            
        
print(total, max_cnt)