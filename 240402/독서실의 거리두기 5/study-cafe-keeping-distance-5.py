n = int(input())
array = list(map(int, list(input())))

def count_num(array):
    check = False
    cnt = 0
    min_cnt = 1e12
    for idx in range(len(array)):
        if check == False:
            if array[idx] == 1:
                check = True
        else:
            if array[idx] == 0:
                cnt += 1
            else:
                cnt += 1
                min_cnt = min(min_cnt, cnt)
                cnt = 0
    return min_cnt
    



    return min_cnt
        
max_cnt = 0
for i in range(n):
    if array[i] == 0:
        array[i] = 1
        max_cnt = max(count_num(array), max_cnt)
        array[i] = 0

print(max_cnt)