n, s = map(int, input().split())
array = list(map(int, input().split()))

min_result = 1e9
for i in range(n):
    for j in range(i+1, n):
        tmp = array[i], array[j]
        array[i] = 0
        array[j] = 0
        min_result = min(abs(sum(array) - s), min_result)
        array[i], array[j] = tmp

print(min_result)