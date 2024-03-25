n, h, t = map(int, input().split())

array = list(map(int, input().split()))

# 연속하게 t번 이상 h 높이..
final_result = 1e9
for i in range(n-t):
    result = 0
    for idx in range(t):
        result += abs(h - array[i + idx])
    final_result = min(final_result, result)

print(final_result)