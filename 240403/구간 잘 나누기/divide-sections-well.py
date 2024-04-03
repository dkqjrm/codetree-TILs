n, m = map(int, input().split())
array = list(map(int, input().split()))

for maxi in range(max(array), 10001): # max
    tmp_result = []
    total = array[0]
    
    for idx in range(1, n):
        if total + array[idx] > maxi:
            tmp_result.append(total)
            total = array[idx]
        else:
            total += array[idx]
    tmp_result.append(total)

    if len(tmp_result) <= m:
        print(maxi)
        break