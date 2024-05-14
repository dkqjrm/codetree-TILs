n, t = map(int, input().split())
lu = list(map(int, input().split())) # 1 2 4
ru = list(map(int, input().split())) # 5 9 3
low = list(map(int, input().split())) # 6 5 1

array = lu + ru + low

while t:
    t -= 1
    tmp = array[-1]
    for i in range(n * 3 - 1, 0, -1):
        array[i] = array[i - 1]
    array[0] = tmp
print(*array[:n])
print(*array[n:2*n])
print(*array[2*n:])