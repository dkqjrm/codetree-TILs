n = int(input())
array = list(map(int, input().split()))

for i in range(1, max(array) + 1): # 첫번째 숫자
    ori_array = [i]

    for j in array:
        if j - ori_array[-1] not in ori_array and j - ori_array[-1] >= 1:
            ori_array.append(j - ori_array[-1])
        else:
            break

    if len(ori_array) == n:
        print(*ori_array)
        break