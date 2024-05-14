n, t = map(int, input().split())
higher = list(map(int, input().split())) # 1 2 3 -> 1 1 2
lower = list(map(int, input().split())) # 6 5 1 -> 3 6 5

array = higher + lower

while t:
    t -= 1
    tmp = array[-1]
    for i in range(n * 2 - 1, 0, -1):
        array[i] = array[i - 1]
    array[0] = tmp
print(*array[:n])
print(*array[n:])