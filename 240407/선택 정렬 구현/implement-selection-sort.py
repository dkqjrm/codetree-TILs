n = int(input())
array = list(map(int, input().split()))



for i in range(n):
    min_index = -1
    for j in range(i, n):
        if min_index == -1 or array[min_index] >= array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(*array)