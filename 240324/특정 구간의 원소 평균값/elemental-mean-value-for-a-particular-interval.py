n = int(input())
array = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in (i + 1, n + 1):
        if sum(array[i:j]) % len(array[i:j]) == 0:
            average = sum(array[i:j]) / len(array[i:j])
            if average in array[i:j]:
                result += 1

print(result)