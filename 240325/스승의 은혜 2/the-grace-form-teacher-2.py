n, b = map(int, input().split())
array = [int(input()) for _ in range(n)]

max_num = 0

for i in range(n):
    array[i] //= 2
    result = 0
    num = 0
    for j in sorted(array):
        if b >= result + j:
            result += j
            num += 1
    max_num = max(num, max_num)
    array[i] *= 2

print(max_num)