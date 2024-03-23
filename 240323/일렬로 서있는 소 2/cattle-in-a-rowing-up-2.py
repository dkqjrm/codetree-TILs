n = int(input())
array = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i + 1, n):
        if array[i] <= array[j]:
            for k in range(j + 1, n):
                if array[j] <= array[k]:
                    result += 1

print(result)