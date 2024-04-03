# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# min_result = 1e12

# for i in range(len(array)):
#     tmp_array = []
#     maxi = sum(array[:i + 1])
#     tmp_array.append(maxi)

#     end = i + 1
#     cnt = 1
#     for j in range(i + 1, len(array)):
#         if sum(array[end:j + 1]) < maxi:
#             tmp_array.append(sum(array[end:j + 1]))
#             end = j - 1

#     if len(tmp_array) == m:
#         min_result = min(min_result, max(tmp_array))

# print(min_result)

# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# min_result = 1e12

# for maxi in range(0, 101): # max
#     end = 0
#     tmp_array = []
#     for i in range(len(array)):
#         if sum(array[end:i + 1]) > maxi:
#             tmp_array.append(sum(array[end:i + 1]))
#             end = i + 1
#         elif i + 1 == n:
#             tmp_array.append(sum(array[end:i + 1]))

#     if len(tmp_array) == m:
#         min_result = min(min_result, max(tmp_array))

# print(min_result)

n, m = map(int, input().split())
array = list(map(int, input().split()))
min_result = 1e12

for maxi in range(max(array), 101): # max
    tmp_result = [0]
    for i in array:
        if tmp_result[-1] + i > maxi:
            tmp_result.append(i)
        else:
            tmp_result[-1] += i

    if len(tmp_result) == m:
        min_result = min(min_result, max(tmp_result))

    print(tmp_result)
print(min_result)