n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]


def check(x):
    for i in array:
        x *= 2
        if x < i[0] or x > i[1]:
            return 0
        
    return 1

min_x = 1e12

for x in range(1, array[0][1]):
    if check(x):
        min_x = min(x, min_x)
    

print(min_x)