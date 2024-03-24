n = int(input())
array = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            result += 1
        else:  
            if sum(array[i:j + 1]) % len(array[i:j + 1]) == 0:
                average = sum(array[i:j + 1]) / len(array[i:j + 1])
                if average in array[i:j + 1]:
                    result += 1
                # print(i, j, average, array[i:j + 1])

print(result)