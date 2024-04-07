n = int(input())
array = list(map(int, input().split()))



for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(*array)