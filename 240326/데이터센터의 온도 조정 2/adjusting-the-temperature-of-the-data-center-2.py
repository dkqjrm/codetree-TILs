n, c, g, h = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

max_result = 0
for temp in range(0, 1001):
    result = 0
    for machine in array:
        machine[0], machine[1]
        if temp < machine[0]:
            result += c
        elif temp <= machine[1]:
            result += g
        else:
            result += h
    
    max_result = max(result, max_result)

print(max_result)