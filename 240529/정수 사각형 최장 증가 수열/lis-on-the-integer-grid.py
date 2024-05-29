n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    global dp
    now = matrix[r][c] # starting point의 value
    for dr, dc in zip(drs, dcs):
        next_r = r + dr
        next_c = c + dc
        if in_range(next_r, next_c) and matrix[next_r][next_c] > now:
            dp[next_r][next_c] = max(dp[next_r][next_c], dp[r][c] + 1)
            dfs(next_r, next_c)
    return

for r in range(n):
    for c in range(n):
        check = False
        # r, c는 스타팅 포인트
        for dr, dc in zip(drs, dcs):
            next_r = r + dr
            next_c = c + dc
            if in_range(next_r, next_c) and matrix[next_r][next_c] < matrix[r][c]:
                check = True
                
        if check is False:
            dfs(r, c)

# for i in dp:
#     print(*i)
print(max(max(dp)))