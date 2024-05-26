n = int(input())
array = list(map(int, input().split()))

max_value = 0

for i in range(n - 1): # 0 ~ 6
    for j in range(i + 1, n + 1):
        tmp_value = sum(array[i:j])
        tmp_value = max(tmp_value, tmp_value - min(array[i:j]))
        max_value = max(max_value, tmp_value)

print(max_value)