array = list(map(int, input().split()))

total = sum(array)

result = 1e9
for i in range(len(array)):
    for j in range(i+1, len(array)):
        for k in range(j+1, len(array)):
            tmp = abs(total - (array[i] + array[j] + array[k]))
            result = min(abs(tmp - (array[i] + array[j] + array[k])), result)
            

print(result)