# 터진 곳을 None으로 하고, 각 column마다 해서 내리면 되지 않을까?

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n 

def bomb(array, r, c):
    number = array[r][c]
    for i in range(number):
        if in_range(r-i, c):
            array[r-i][c] = None
        if in_range(r+i, c):
            array[r+i][c] = None
        if in_range(r, c-i):
            array[r][c-i] = None
        if in_range(r, c+i):
            array[r][c+i] = None
    return array

def sorting(array):
    for col in range(len(array)):
        tmp_arr = []
        for row in range(len(array)):
            if array[row][col] != None:
                tmp_arr.append(array[row][col])
        while len(tmp_arr) != n:
            tmp_arr = [0] + tmp_arr
        for row in range(len(array)):
            array[row][col] = tmp_arr[row]
    return array


            
        



array = bomb(array, r, c)
array = sorting(array)

for i in array:
    print(*i)