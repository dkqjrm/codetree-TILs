n, m = map(int, input().split())
array = list(map(int, input().split()))
min_result = 1e12

for maxi in range(0, 100): # max
    tmp_result = [array[0]]
    for idx in range(0, len(array)):
        if tmp_result[-1] + array[idx] > maxi:
            tmp_result.append(array[idx])
        else:
            tmp_result[-1] += array[idx]

    if len(tmp_result) <= m:
        min_result = min(min_result, max(tmp_result))
    # print(maxi, tmp_result, len(tmp_result))
print(min_result)