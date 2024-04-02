n = int(input())
array = list(map(int, list(input())))

def check(array):
    check = False
    min_cnt = 1e12
    for i in array:
        if check is False and i == 1:
            check = True
            cnt = 0
        elif check is True and i == 0:
            cnt += 1
        elif check is True and i == 1:
            cnt += 1
            min_cnt = min(cnt, min_cnt)
            cnt = 0
    return min_cnt


max_cnt = 0

for i in range(n):
    for j in range(i, n):
        
        if i != j and array[i] == 0 and array[j] == 0:
            array[i] = 1
            array[j] = 1
            cnt = check(array)
            max_cnt = max(cnt, max_cnt)
            array[i] = 0
            array[j] = 0
        
print(max_cnt)