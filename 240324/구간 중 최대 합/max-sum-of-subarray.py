n, k = map(int, input().split())
array = list(map(int, input().split()))

max_result = 0
for i in range(0, n - k + 1):
    max_result = max(max_result, sum(array[i:i+k]))

print(max_result)