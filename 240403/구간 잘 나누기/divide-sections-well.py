n, m = map(int, input().split())
array = list(map(int, input().split()))
min_result = 1e12

for maxi in range(1, 10001): # max
    tmp_result = [0]
    for i in array:
        if tmp_result[-1] + i > maxi:
            tmp_result.append(i)
        else:
            tmp_result[-1] += i

    if len(tmp_result) <= m:
        min_result = min(min_result, max(tmp_result))

    # print(tmp_result)
print(min_result)