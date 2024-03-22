n = int(input())

matrix = [input() for _ in range(n)]

k = int(input())

dr = [0, 1, 0, -1] # 동 남 서 북
dc = [1, 0, -1, 0] # 동 남 서 북
# 무조건 한칸이동

def in_range(r, c, n):
    return 1 <= r and r <= n and 1 <= c and c <= n

r, c = 1, 0

direction = 0
for i in range(k):
    move_r = r + dr[direction]
    move_c = c + dc[direction]
    
    if in_range(move_r, move_c, n):
        r = move_r
        c = move_c
    else:
        direction = (direction + 1) % 4

arrow = (k - 1) // n

cnt = 0

while in_range(r, c, n):
    # print(r, c, arrow)
    what = matrix[r-1][c-1]
    # print(what)
    if what == '\\':
        if arrow == 0:
            r += dr[arrow]
            c += dc[arrow]
            arrow = 3
        elif arrow == 1:
            r += dr[3]
            c += dc[3]
            arrow = 2
        elif arrow == 2:
            r += dr[arrow]
            c += dc[arrow]
            arrow = 1
        else:  
            r += dr[1]
            c += dc[1]
            arrow = 0
    elif what == '/':
        if arrow == 0:
            r += dr[2]
            c += dc[2]
            arrow = 1
        elif arrow == 1:
            r += dr[arrow]
            c += dc[arrow]
            arrow = 0
        elif arrow == 2:
            r += dr[0]
            c += dc[0]
            arrow = 3
        else:  
            r += dr[arrow]
            c += dc[arrow]
            arrow = 2
    cnt += 1
    
print(cnt)




# k = 1 -> 0,0 상
# k = 2 -> 1,0 상
# k = 3 -> 2,0 상
# k = 4 -> 2,0 우
# k = 5 -> 2,1 우
# k = 6 -> 2,2 우
# k = 7 -> 2,2 하
# k = 8 -> 1,2 하
# k = 9 -> 0,2 하
# k = 10 -> 0,2 좌
# k = 11 -> 0,1 좌
# k = 12 -> 0,0 좌