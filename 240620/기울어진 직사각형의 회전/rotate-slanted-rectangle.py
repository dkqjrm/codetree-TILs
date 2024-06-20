n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, direction = map(int, input().split())

def rotate_matrix(r, c, m1, m2, m3, m4, direction):
    if direction == 0:  # 시계 방향
        drs = [-1, -1, 1, 1] # 우상, 좌상, 좌하, 우하
        dcs = [1, -1, -1, 1]

    elif direction == 1:  # 반시계 방향
        drs = [-1, 1, 1, -1]  # 우상, 우하, 좌하, 좌상
        dcs = [1, 1, -1, -1]
        # r과 c의 위치를 좌상한 곳으로 이동
        r += (drs[3] * m4)
        c += (dcs[3] * m4)

        
    
    # 지금거 저장, 다음오로 넘어가서 다음거 저장, 다음거에 지금거 넣기
    prev_num = array[r][c]

    for _ in range(m1):
        # print(array[r][c])
        # print(r, c)
        r += drs[0]
        c += dcs[0]
        tmp = array[r][c]
        array[r][c] = prev_num
        prev_num = tmp

    for _ in range(m2):
        # print(array[r][c])
        # print(r, c)
        r += drs[1]
        c += dcs[1]
        tmp = array[r][c]
        array[r][c] = prev_num
        prev_num = tmp

    for _ in range(m3):
        # print(array[r][c])
        # print(r, c)
        r += drs[2]
        c += dcs[2]
        tmp = array[r][c]
        array[r][c] = prev_num
        prev_num = tmp

    for _ in range(m4):
        # print(array[r][c])
        # print(r, c)
        r += drs[3]
        c += dcs[3]
        tmp = array[r][c]
        array[r][c] = prev_num
        prev_num = tmp

    for i in array:
        print(*i)

rotate_matrix(r - 1, c - 1, m1, m2, m3, m4, direction)