n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
arrows = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

r -= 1 
c -= 1
# dfs?
max_cnt = 0
cnt = 0

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def solve(r, c):
    global max_cnt
    global cnt
    # print(r, c)
    
    max_cnt = max(cnt, max_cnt)
    number = matrix[r][c]
    arrow = arrows[r][c]
    if arrow == 1:
        for i in range(1, n + 1):
            if in_range(r - i, c) and matrix[r - i][c] > number:
                cnt += 1
                solve(r - i, c)
                cnt -= 1

    elif arrow == 2:
        for i in range(1, n + 1):
            if in_range(r - i, c + i) and matrix[r - i][c + i] > number:
                cnt += 1
                solve(r - i, c + i)
                cnt -= 1
    elif arrow == 3:
        for i in range(1, n + 1):
            if in_range(r, c + i) and matrix[r][c + i] > number:
                cnt += 1
                solve(r, c + i)
                cnt -= 1
    elif arrow == 4:
        for i in range(1, n + 1):
            if in_range(r + i, c + i) and matrix[r + i][c + i] > number:
                cnt += 1
                solve(r + i, c + i)
                cnt -= 1
    elif arrow == 5:
        for i in range(1, n + 1):
            if in_range(r + i, c) and matrix[r + i][c] > number:
                cnt += 1
                solve(r + i, c)
                cnt -= 1
    elif arrow == 6:
        for i in range(1, n + 1):
            if in_range(r + i, c - i) and matrix[r + i][c - i] > number:
                cnt += 1
                solve(r + i, c - i)
                cnt -= 1
    elif arrow == 7:
        for i in range(1, n + 1):
            if in_range(r, c - i) and matrix[r][c - i] > number:
                cnt += 1
                solve(r, c - i)
                cnt -= 1
    elif arrow == 8:
        for i in range(1, n + 1):
            if in_range(r - i, c - i) and matrix[r - i][c - i] > number:
                cnt += 1
                solve(r - i, c - i)
                cnt -= 1

    return

solve(r, c)
print(max_cnt)