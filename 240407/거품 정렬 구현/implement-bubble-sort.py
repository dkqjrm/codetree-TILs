n = int(input())

array = list(map(int, input().split()))

for _ in range(n-1):
    for i in range(n - 1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
        

print(*array)