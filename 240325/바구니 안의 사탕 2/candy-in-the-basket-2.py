n, k = map(int, input().split())

array = [0] * 105 
for _ in range(n):
    num, location = map(int, input().split())
    array[location] += num

result = 0
for i in range(k, len(array) - k - 1):
    result = max(result, sum(array[i - k: i + k + 1]))
    # print(array[i - k: i + k + 1], i - k, i + k + 1)

print(result)